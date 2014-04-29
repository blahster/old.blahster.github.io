#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Blahster'
SITENAME = u'Blahster'
SITEURL = ''

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['ipythonnb']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../pelican-bootstrap3'
PYGMENTS_STYLE = 'default'
# PYGMENTS_STYLE='friendly'

# For pelican-ootstrap3
#BOOTSTRAP_THEME = 'simplex'
BOOTSTRAP_THEME = 'spacelab'
# nice but, background doesn't work well with code as is
#BOOTSTRAP_THEME = 'superhero'
#BOOTSTRAP_THEME = 'cosmo'
DISPLAY_BREADCRUMBS = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DISQUS_SITENAME = "doubleblahster"


