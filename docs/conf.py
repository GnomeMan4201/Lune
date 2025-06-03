project = 'LUNE'
author = 'GnomeMan4201'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary'
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']import os, sys; sys.path.insert(0, os.path.abspath('lune'))
