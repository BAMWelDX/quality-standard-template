# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Local build command ------------------------------------------------------------------

# sphinx-build -W -n -b html -d docs/_build/doctrees docs docs/_build/html --keep-going

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(""))
sys.path.insert(0, os.path.abspath("../src"))

from {{cookiecutter.project_slug}}._version import __version__

# -- Project information -----------------------------------------------------

project = "{{ cookiecutter.project_slug }}"
copyright = f"{datetime.now().year}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"

# The full version, including alpha/beta/rc tags
release = __version__

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinxcontrib.bibtex",
    "sphinx_copybutton",
    "sphinx_asdf",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = "_static/logo.svg"
#html_favicon = "_static/logo.ico"

html_theme_options = {
    "external_links": [{"url": "https://weldx.readthedocs.io/", "name": "WelDX"}],
    "github_url": "{{ cookiecutter.url }}",
    "use_edit_page_button": False,
    "show_prev_next": False,
}

html_context = {
    "github_user": "BAMWelDX",
    "github_repo": "weldx",
    "github_version": "master",
    "doc_path": "docs",
}

# --------------------------------------------------------------------------------------

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build/*"]

# -- sphinx-asdf configuration -------------------------------------------------
# This variable indicates the top-level directory containing schemas.
# The path is relative to the location of conf.py in the package
asdf_schema_path = "../resources"
# This variable indicates the standard prefix that is common to all schemas
# provided by the package.
asdf_schema_standard_prefix = "{{ cookiecutter.organization_name }}"


# enable references to the ASDF Standard documentation
asdf_schema_reference_mappings = [
    (
        "tag:stsci.edu:asdf",
        "http://asdf-standard.readthedocs.io/en/latest/generated/stsci.edu/asdf/",
    ),
    (
        "tag:weldx.bam.de:weldx",
        "http://weldx.readthedocs.io/en/latest/generated/weldx.bam.de/weldx/",
    ),
]
