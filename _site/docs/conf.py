# -*- coding: utf-8 -*-
#

from recommonmark.transform import AutoStructify
import ablog
import sys
import os

# Only for windows compatability - Forces default encoding to UTF8, which it may not be on windows
if os.name == 'nt':
    reload(sys)
    sys.setdefaultencoding('UTF8')


sys.path.append(os.getcwd())  # noqa

from _ext.core import (
    add_jinja_filters, rstjinja, override_page_template, load_conference_data,
    set_html_context, unset_html_context
)
from _ext.meetups import MeetupListing
from _ext.videos import main


exclude_patterns = [
    '_build',
    'include',
    '_data',
    'node_modules',
]

# Only build the videos on production, to speed up dev
on_rtd = os.environ.get('READTHEDOCS') == 'True'
on_netlify = os.environ.get('BUILD_VIDEOS') == 'True'
on_travis = os.environ.get('TRAVIS') == 'True'
if not on_rtd and not on_netlify and not on_travis:
    exclude_patterns.append('videos')

extensions = [
    'ablog',
    'sphinxcontrib.datatemplates',
    'recommonmark',
]
blog_baseurl = 'http://www.writethedocs.org/'
blog_path = 'blog/archive'
blog_authors = {
    'Team': ('Write the Docs Team', 'http://www.writethedocs.org/team/'),
    'eric': ('Eric Holscher', 'http://ericholscher.com'),
    'kelly': ("Kelly O'Brien", 'https://twitter.com/OBrienEditorial'),
}
blog_default_author = 'Team'
blog_feed_archives = True
blog_feed_fulltext = True
blog_feed_length = 10
blog_locations = {
    'PDX': ('Portland, Oregon', 'http://www.portlandhikersfieldguide.org/'),
}
blog_default_location = 'PDX'
fontawesome_link_cdn = 'https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css'

templates_path = ['_templates', 'include']
templates_path.append(ablog.get_html_templates_path())

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
    'sidebar_includehidden': False,
    'github_user': 'writethedocs',
    'github_repo': 'www',
    'github_banner': True,
    'github_button': False,
}

html_favicon = '_static/favicon/favicon-96x96.png'
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

# Our additions

html_context = {
    'conf_py_root': os.path.dirname(os.path.abspath(__file__)),
    'conferences': load_conference_data(),
}

# Uncomment this line to generate videos
#html_context.update(main())

# html_experimental_html5_writer = True

def setup(app):
    # Set up our custom jinja filters
    app.connect("builder-inited", add_jinja_filters)

    # Transform RST with Jinja, using proper context
    app.connect("source-read", rstjinja)

    # Adjust html_context properly for datatemplate processing
    app.connect("source-read", set_html_context)
    app.connect("doctree-read", unset_html_context)

    # Render HTML templates with proper HTML context
    app.connect('html-page-context', override_page_template)

    app.add_directive('meetup-listing', MeetupListing)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        # 'enable_auto_doc_ref': True,
        'enable_eval_rst': True,
    }, True)
    app.add_transform(AutoStructify)
    app.add_stylesheet('css/global-customizations.css')
