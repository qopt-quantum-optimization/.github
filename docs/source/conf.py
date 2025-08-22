# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Quantum Optimization Toolkit'
copyright = '2025, Xinpeng Li, Ji Liu, Jeffrey Larson, Matt Menickelly, Kwassi Joseph Dzahini, Zain Saleem, Paul Hovland'
author = 'Xinpeng Li, Ji Liu, Jeffrey Larson, Matt Menickelly, Kwassi Joseph Dzahini, Zain Saleem, Paul Hovland'
release = '0.1.0-alpha'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
    'sphinxcontrib.bibtex',
]

bibtex_bibfiles = ['refs.bib']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ['_static']
html_theme = 'furo'
html_theme_options = {
    "light_logo": "logo-light.png",
    "dark_logo": "logo-dark.png",
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    # Optional color overrides
    "light_css_variables": {
        "color-brand-primary": "#005293",
        "color-brand-content": "#005293",
    },
}
