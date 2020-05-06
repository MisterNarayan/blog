#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shiva Saxena'
SITENAME = 'Mister Narayan'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# My additions
THEME = '/home/shiva/.virtualenvs/blog/lib/python3.8/site-packages/pelican/themes/pelican-clean-blog'
FAVICON = 'blog/favicon.ico'
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/misternarayan'),
          ('github', 'https://github.com/misternarayan'),
          ('gitlab', 'https://gitlab.com/misternarayan'),
          ('bitbucket', 'https://bitbucket.com/misternarayan'),
          ('instagram', 'https://instagram.com/misternarayan'),
          ('youtube', 'https://www.youtube.com/channel/UCTEqqhjtL1cioJKDhj6fx3w'),
          ('envelope','mailto:shivanarayansaxena@gmail.address'))

SITESUBTITLE = 'Open Source Lover | Software Developer'
