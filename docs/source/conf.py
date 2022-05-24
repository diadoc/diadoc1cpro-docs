# -*- coding: utf-8 -*-

from sys import path as PATH_variable
from os import path
import pathlib as pl

html_static_path = ['_static']
html_style = 'css/diadoc 1C style.css'

templates_path = ['_templates']

source_suffix = '.rst'
exclude_patterns = []

master_doc = 'DocumentationRelocation'

project = u'Диадок 1С'
copyright = u'2018, Diadoc'
author = u'Diadoc'
version = ''
release = ''
language = 'ru'

htmlhelp_basename = 'Диадок'
todo_include_todos = False
html_show_sphinx = False
html_theme = 'sphinx_rtd_theme'
pygments_style = 'vs'
html_search_language = 'ru'

html_copy_source = False
