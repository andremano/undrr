# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'undrr'
copyright = '2025, André da Silva Mano (editor), Cees van Vesten (coordination), Nanette Kingma, Elinor Meredith, Irene Manzella and Catherine Nabukulu'
author = 'André da Silva Mano (editor), Cees van Vesten (coordination), Nanette Kingma, Elinor Meredith, Irene Manzella and Catherine Nabukulu'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'

#html_theme = 'alabaster'
html_static_path = ['_static']
