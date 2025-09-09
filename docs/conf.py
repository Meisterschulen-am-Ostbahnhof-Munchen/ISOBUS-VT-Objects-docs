# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ISOBUS Virtual Terminal: Benutzeroberfläche und Objekte (2)"
copyright = "2022-2025, Meisterschulen am Ostbahnhof - München"
author = "Franz Höpfinger"

html_baseurl = "https://docs.ms-muc-docs.de/projects/isobus-vt-objects-docs"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinxcontrib.googleanalytics",
    "sphinx_rtd_size",
]

sphinx_rtd_size_width = "90%"

version = "0.0.2"
release = version
templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "CHANGELOG.rst"]


# -- MyST settings ---------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
]
myst_heading_anchors = 7

googleanalytics_id = 'G-4WPKCFX4NN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
