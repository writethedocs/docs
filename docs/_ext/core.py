from __future__ import print_function
from future import standard_library
standard_library.install_aliases()

import os
import io
import re
import yaml
import glob

import CommonMark

try:
    from pathlib import PurePath
except ImportError:
    from pathlib2 import PurePath

try:
    # Python 2.6-2.7
    from html.parser import HTMLParser
except ImportError:
    # Python 3
    from html.parser import HTMLParser


def load_yaml(path):
    with io.open(path, encoding='utf-8') as fp:
        return yaml.safe_load(fp)


def load_page_yaml_data(app, page):
    """
    Get conference specific YAML data.

    Returns an empty dict if it isn't run on a proper conference page.
    """
    data = {}
    if page.startswith('conf'):
        p = PurePath(page)
        try:
            year = int(p.parts[2])
        except (ValueError, IndexError):
            return data
        if year >= 2018:
            yaml_config = load_yaml('_data/config-' + p.parts[1] + '-' + p.parts[2] + '.yaml')
            data.update(yaml_config)
    return data


def slugify(slug):
    slug = slug.encode('utf-8', 'ignore').lower().decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


def generate_video_slug(session):
    if 'title' not in session:
        return u''
    title = session['title']
    for speaker in session.get('speakers', []):
        title += '-{}'.format(speaker.get('slug', speaker['name']))
    return slugify(title)


def normalize_session(session):
    youtube_pattern = re.compile(r'https://www.youtube.com/watch\?v=(.+)')

    session['slug'] = generate_video_slug(session)
    if 'video' in session and 'youtube.com' in session['video']:
        mo = youtube_pattern.match(session['video'])
        if mo:
            session['youtubeId'] = mo.group(1)


def rstjinja(app, docname, source):
    """
    Render our conf pages as a jinja template for more goodness.
    """
    if getattr(app.builder, 'implementation', None) or app.builder.format != 'html':
        return

    """
    Only load yaml config for 2018 and onwards
    """
    context = load_page_yaml_data(app, docname)
    context.update(app.config.html_context)
    if docname.startswith(('conf/', 'guide/', 'videos/by-year', 'videos/by-series')):
        src = source[0]
        rendered = app.builder.templates.render_string(src, context)
        source[0] = rendered


def add_jinja_filters(app):
    if getattr(app.builder, 'implementation', None) or app.builder.format != 'html':
        return

    from .meetups import state_abbr

    def markdown_filter(data):
        parser = CommonMark.DocParser()
        renderer = CommonMark.HTMLRenderer()
        return renderer.render(parser.parse(data))

    def html_unescape(str):
        h = HTMLParser()
        return h.unescape(str)

    app.builder.templates.environment.filters['markdown'] = markdown_filter
    app.builder.templates.environment.filters['html_unescape'] = html_unescape
    app.builder.templates.environment.filters['state_abbr'] = state_abbr
    app.builder.templates.environment.filters['slugify'] = slugify


def override_page_template(app, pagename, templatename, context, doctree):
    """
    Set the template to use when rendering the page.

    If a string is returned from this function,
    it will be the template used to render this page.
    Example::

        :template: 2018/conf.html

        Page title
        ==========

        Content
    """
    page_context = load_page_yaml_data(app, pagename)
    context.update(page_context)

    # Markdown
    if (context and
            'page_source_suffix' in context and
            context['page_source_suffix'] == '.md'):
        txt = doctree[0].astext()
        if txt.startswith(':template:'):
            context['body'] = context['body'].replace(txt, '')
            return txt.split(':')[2].strip()
    # rst
    try:  # Sphinx was throwing a weird error here, and this is a workaround
        if (context and
                'meta' in context and
                'template' in context.get('meta', {})):
            return context['meta']['template']
    except TypeError:
        pass


def load_conference_data():
    speakers_file_pattern = re.compile(r'(\d{4}).(\w+).speakers')
    sessions_file_pattern = re.compile(r'(\w+)-(\d{4})-day-(\d+)')
    result = {}
    for f in glob.glob('_data/*.yaml'):
        base = os.path.basename(f)
        base, _ = os.path.splitext(base)
        # Only consider conference data files that are following the common
        # naming convention and log everything out as warning.
        mo = speakers_file_pattern.match(base)
        if mo:
            year = int(mo.group(1))
            region = mo.group(2)
            if year not in result:
                result[year] = {}
            if region not in result[year]:
                result[year][region] = {}
            result[year][region]['speakers'] = load_yaml(f)
            for session in result[year][region]['speakers']:
                normalize_session(session)
                session['year'] = year
                session['series'] = u'Write the Docs {}'.format(region.upper())
                session['series_slug'] = region
                session['event'] = u'Write the Docs {} {}'.format(region.upper(), year)
                session['path'] = 'conf/{series_slug}/{year}/videos/{slug}'.format(**session)
            continue
        mo = sessions_file_pattern.match(base)
        if mo:
            continue
        #print("%s doesn't follow the conference data file conventions" % (base,))
    return result


def set_html_context(app, docname, source):
    # Store old context
    page_context = load_page_yaml_data(app, docname)
    if page_context:
        app.config.old_html_context = app.config.html_context.copy()
        app.config.html_context.update(page_context)


def unset_html_context(app, doctree):
    if hasattr(app.config, 'old_html_context'):
        app.config.html_context = app.config.old_html_context.copy()
        del app.config.old_html_context
