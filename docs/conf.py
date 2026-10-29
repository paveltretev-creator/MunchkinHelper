"""
Конфигурация Sphinx для документации Munchkin Helper
"""
import os
import sys

# Пути к модулям проекта (относительно расположения conf.py)
_docs_dir = os.path.dirname(os.path.abspath(__file__))
_project_dir = os.path.dirname(_docs_dir)

sys.path.insert(0, os.path.join(_project_dir, 'backend'))
sys.path.insert(0, os.path.join(_project_dir, 'frontend'))

# -- Project information -----------------------------------------------------
project = 'Munchkin Helper'
copyright = '2026, Ваше имя'
author = 'Ваше имя'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for autodoc -----------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',
}

autodoc_typehints = 'description'

# -- Napoleon settings -------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True