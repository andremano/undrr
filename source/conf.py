# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'undrr'
copyright = 'University of Twente, 2025'
author = 'André da Silva Mano (editor), Cees van Vesten (scientific coordination), Nanette Kingma, Elinor Meredith, Irene Manzella and Catherine Nabukulu'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

sys.path.append(os.path.abspath("./_ext"))

# Name of the master document.
master_doc = 'index'

extensions = ['sphinx_design'] #requires pip install sphinx-design (to allow for dropdown admonitions)

templates_path = ['_templates']
exclude_patterns = ['_static/assets/external_links.rst', '_static/assets/data-links.rst']

numfig = True

link_file = ['_static/assets/external_links.rst',
            '_static/assets/data-links.rst'
            ]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
#html_theme = 'alabaster'

# Allows storing external links in separated rst
rst_epilog=""

# Target link-files
link_files = ['_static/assets/external_links.rst',
            '_static/assets/data-links.rst'
            ]

# Read links in the from the target files
for file in link_files:
    with open(file) as f:
        rst_epilog += f.read()


html_static_path = ['_static']

# Configure paper size, font size, preamble options, etc (for LaTeX output).
latex_elements = {
    'figure_align': 'H',
    'preamble': '''
        \\usepackage{float}
        ''',
}
