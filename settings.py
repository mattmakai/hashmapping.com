# -*- coding: utf-8 -*-

AUTHOR = u'Matt Makai'
SITENAME = u'Hashmapping'
SITEURL = 'http://www.hashmapping.com'
TIMEZONE = 'America/New_York'

GITHUB_URL = 'https://github.com/makaimc/hashmapping.com'
PDF_GENERATOR = False

DIRECT_TEMPLATES = ('index', 'sitemap', 'table-of-contents', 'blog', 'all')

ARTICLE_SAVE_AS = 'blog/{slug}.html'

SITEMAP_SAVE_AS = 'sitemap.xml'

FEED_DOMAIN = 'http://www.hashmapping.com'
FEED_RSS = 'feed'

BYLINE = '&copy; 2016 Matt Makai. All Rights Reserved.'
LINKS = ()

MARKUP = ('rst', 'markdown',)

SOCIAL = (
    ('Email', 'mailto:matthew.makai@gmail.com'),
    ('GitHub', 'https://github.com/makaimc'),
    ('Twitter', 'http://twitter.com/mattmakai'),
)

PROJECTS = ()

JINJA_EXTENSIONS = (['jinja2.ext.autoescape',])

