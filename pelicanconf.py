#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'anonymous'
SITENAME = u'change_code'
SITESUBTITLE = u'To improve is to change<br/>To be perfect is to have changed often<br/>—Sir Winston Churchill'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['.']
IGNORE_FILES = ['.#*', '*~']

THEME = 'blue-penguin'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
  (u'Projects', 'projects.html'),
  (u'Erlang', 'erlang.html'),
]

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = False
DAY_ARCHIVE_SAVE_AS = False

DEFAULT_CATEGORY = 'misc'
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
CATEGORY_SAVE_AS = False
CATEGORIES_SAVE_AS = False

AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
  (u"example", "http://example.com/")
]

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
