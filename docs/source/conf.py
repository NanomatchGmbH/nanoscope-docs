# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Nanoscope'
copyright = '2024, Nanomatch GmbH'
author = 'Nanomatch GmbH'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']


templates_path = ['_templates']
exclude_patterns = []


redirects = {
     "index": "home/home.html"
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'collapse_navigation': True,
    'navigation_depth': 2,  # Adjust depth as needed
}

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "NanomatchGmbH",  # GitHub username
    "github_repo": "nanoscope-docs",  # Repository name
    "github_version": "main",  # Branch name
    "conf_py_path": "/docs/source/",  # Path to your documentation folder
}
