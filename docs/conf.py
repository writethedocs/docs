# -*- coding: utf-8 -*-
#
import CommonMark
import collections
import glob
import io
import os
import json
import re
import yaml

from docutils.parsers import rst
from docutils import nodes
from docutils.statemachine import ViewList
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from sphinx.util.nodes import nested_parse_with_titles
import ablog


exclude_patterns = [
    '_build',
    'include',
    '_data',
]
extensions = [
    'ablog',
    'sphinxcontrib.datatemplates',
]
blog_baseurl = 'http://www.writethedocs.org/blog/'
blog_path = 'blog/archive'
blog_authors = {
    'Team': ('Write the Docs Team', 'http://www.writethedocs.org/team/'),
    'eric': ('Eric Holscher', 'http://ericholscher.com'),
    'kelly': ("Kelly O'Brien", 'https://twitter.com/OBrienEditorial'),
}
blog_default_author = 'Team'

blog_locations = {
    'PDX': ('Portland, Oregon', 'http://www.portlandhikersfieldguide.org/'),
}
blog_default_location = 'PDX'
fontawesome_link_cdn = 'http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css'

templates_path = ['_templates']
templates_path.append(ablog.get_html_templates_path())

source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'Write the Docs'
copyright = u'2016, The Write the Docs Community'
author = u'The Write the Docs Community'

version = '1.0'
release = '1.0'
language = 'en'
html_search_language = 'en'
pygments_style = 'sphinx'
primary_domain = None

html_theme = 'alabaster'
html_theme_options = {
    'logo': 'sticker-wtd-colors.png',
    'github_button': False,
    'sidebar_includehidden': False,
}

html_favicon = '_static/img/favicon.ico'
html_title = 'Write the Docs'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'postcard.html',
        'info.html',
        'navigation.html',
        # 'relations.html',
        # 'searchbox.html',
    ]
}

# Output formats

htmlhelp_basename = 'WritetheDocsdoc'

latex_documents = [
    (master_doc, 'WritetheDocs.tex', u'Write the Docs Documentation',
     u'Eric Holscher \\& the Write the Docs Community', 'manual'),
]

man_pages = [
    (master_doc, 'writethedocs', u'Write the Docs Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'WritetheDocs', u'Write the Docs Documentation',
     author, 'WritetheDocs', 'One line description of project.',
     'Miscellaneous'),
]

suppress_warnings = ['image.nonlocal_uri']


# Our fancy additions

def slugify(slug):
    slug = slug.encode('utf-8', 'ignore').lower().decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


def transform_speakers(speakers):
    for talk in speakers:
        for speaker in talk['speakers']:
            if os.path.exists('_static/img/speakers/%s.jpg' % speaker['slug']):
                speaker['img_file'] = '%s.jpg' % speaker['slug']
            elif os.path.exists('_static/img/speakers/%s.png' % speaker['slug']):
                speaker['img_file'] = '%s.png' % speaker['slug']
            else:
                speaker['img_file'] = 'missing.jpg'


def load_yaml(path):
    with io.open(path, encoding='utf-8') as fp:
        return yaml.safe_load(fp)

def load_meetups_by_region():
    result = collections.defaultdict(list)
    for yaml_file in glob.glob('_data/meetups/*.yaml'):
        meetup = load_yaml(yaml_file)
        if not 'website' in meetup:
            raise SphinxError('Meetup needs a website')
        result[meetup['region']].append(meetup)
    for _, meetups in result.items():
        meetups.sort(key=lambda m : m.get('city', m['country']))
    return result


na_2015_speakers = load_yaml('_data/2015.na.speakers.yaml')
na_speakers = load_yaml('_data/2016.na.speakers.yaml')
na_2017_speakers = load_yaml('_data/2017.na.speakers.yaml')
na_day1 = load_yaml('_data/na-2016-day-1.yaml')
na_day2 = load_yaml('_data/na-2016-day-2.yaml')

eu_2017_speakers = load_yaml('_data/2017.eu.speakers.yaml')
eu_speakers = load_yaml('_data/2016.eu.speakers.yaml')
eu_day1 = load_yaml('_data/eu-2016-day-1.yaml')
eu_day2 = load_yaml('_data/eu-2016-day-2.yaml')

meetups_by_region = load_meetups_by_region()

for list_o_speakers in [na_speakers, eu_speakers, na_2017_speakers, eu_2017_speakers]:
    transform_speakers(list_o_speakers)

for talk in na_day1 + na_day2:
    # Old NA hacks
    if 'Tim Nugent' in talk['Session']:
        talk['speaker'] = 'Tim Nugent'
        talk['slug'] = 'tim-nugent'
    else:
        speaker = talk['Session'].split('-')[-1]
        speaker = speaker.split(',')[0]
        speaker = speaker.split('&')[0]
        talk['speaker'] = speaker.strip()
        slug = slugify(speaker)
        talk['slug'] = slug.strip()

for talk in eu_day1 + eu_day2:
    speaker = talk['Session'].split('-')[0]
    speaker = speaker.split(',')[0]
    speaker = speaker.split('&')[0]
    talk['speaker'] = speaker.strip()
    slug = slugify(speaker)
    talk['slug'] = slug.strip()

    # slug hacks
    if 'Kata' in talk['Session']:
        talk['slug'] = 'kata-nagygyorgy'
    if 'native speaker' in talk['Session']:
        talk['slug'] = 'istvan-zoltan-szabo'


html_context = {
    'na_2015_speakers': na_2015_speakers,
    'eu_2016_speakers': eu_speakers,
    'na_2016_speakers': na_speakers,
    'na_2017_speakers': na_2017_speakers,
    'eu_2017_speakers': eu_2017_speakers,
    'na_2016_day1': na_day1,
    'na_2016_day2': na_day2,
    'eu_2016_day1': eu_day1,
    'eu_2016_day2': eu_day2,
    'conf_py_root': os.path.dirname(os.path.abspath(__file__)),
    'meetups_by_region': meetups_by_region,
}

state_abbreviations = {
    'Canada': {
        'Ontario': 'ON',
    },
    'USA': {
        'California': 'CA',
        'Colorado': 'CO',
        'Idaho': 'ID',
        'Massachusetts': 'MA',
        'New York': 'NY',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Texas': 'TX',
        'Washington': 'WA',
    }
}


def on_page_context(app, pagename, templatename, context, doctree):
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


def rstjinja(app, docname, source):
    """
    Render our conf pages as a jinja template for more goodness.
    """
    if getattr(app.builder, 'implementation', None) or app.builder.format != 'html':
        return
    if docname.startswith('conf/') or docname.startswith('guide/'):
        src = source[0]
        rendered = app.builder.templates.render_string(src, app.config.html_context)
        source[0] = rendered


def add_jinja_filters(app):
    if getattr(app.builder, 'implementation', None) or app.builder.format != 'html':
        return
    def markdown_filter(data):
        parser = CommonMark.DocParser()
        renderer = CommonMark.HTMLRenderer()
        return renderer.render(parser.parse(data))
    def state_abbr(meetup):
        states = state_abbreviations.get(meetup['country'])
        if not states:
            return meetup['state']
        return states.get(meetup['state'], meetup['state'])
    app.builder.templates.environment.filters['markdown'] = markdown_filter
    app.builder.templates.environment.filters['state_abbr'] = state_abbr
    app.builder.templates.environment.filters['slugify'] = slugify


class MeetupListing(rst.Directive):
    option_spec = {
        'region': rst.directives.unchanged,
    }
    has_content = False

    def run(self):
        env = self.state.document.settings.env
        app = env.app
        builder = app.builder

        templates = getattr(builder, 'templates', None)
        if not templates:
            return []

        region_name = self.options['region']
        output = ViewList()
        template_name = 'include/meetups/listing.jinja'
        rendered = builder.templates.render(template_name, {
            'meetups': meetups_by_region[region_name],
        })
        for line in rendered.splitlines():
            output.append(line, 'meetup-data')
        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, output, node)
        return node.children


def setup(app):
    app.connect('html-page-context', on_page_context)
    app.connect("source-read", rstjinja)
    app.connect("builder-inited", add_jinja_filters)
    app.add_directive('meetup-listing', MeetupListing)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_auto_doc_ref': True,
        'enable_eval_rst': True,
    }, True)
    app.add_transform(AutoStructify)
    app.add_stylesheet('css/global-customizations.css')
