# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import ltb

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_panels',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'numpydoc',
    'sphinx_copybutton',
    'myst_nb',
    ]

plot_html_show_source_link = False
plot_html_show_formats = False

autosummary_generate = True
numpydoc_show_class_members = False

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'LTB'
copyright = '2023, CURENT LTB'
author = 'CURENT LTB'

# The short X.Y version.
version = ltb.__version__
# The full version, including alpha/beta/rc tags.
release = ltb.__version__

language = "en"

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "use_edit_page_button": True,
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "CURENT",
    "github_repo": "ltb",
    "github_version": "master",
    "doc_path": "docs/source",
}

html_static_path = ['_static']

htmlhelp_basename = 'ltb'


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'matplotlib': ('https://matplotlib.org', None),
}

jupyter_execute_notebooks = "off"

panels_add_bootstrap_css = False
