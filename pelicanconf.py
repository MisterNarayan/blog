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
FAVICON = 'favicon.ico'
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}

# Social widget
SOCIAL = (
          ('github', 'https://github.com/misternarayan'),
          ('twitter', 'https://twitter.com/misternarayan'),
          ('youtube', 'https://www.youtube.com/channel/UCTEqqhjtL1cioJKDhj6fx3w'),
          ('wordpress', 'https://misternarayan.wordpress.com'),
         )


SITESUBTITLE = 'A Pelican Blog by Shiva Saxena'
SHOW_SITESUBTITLE_IN_HTML = 'True'
HEADER_PAGE_TITLE = 'A Pelican Blog'
SHOW_CREDIT_BY_AUTHOR = 'True'
NAVBAR_BRAND = 'Mister Narayan'
BLOG_MENU_CLASS = 'active'

