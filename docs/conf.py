# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime
import os

import requests
from docutils import nodes
from docutils.nodes import Element
from sphinx.writers.html import HTMLTranslator


# Force all external links to open as new tabs,
# without breaking internal links. This causes
# external links to work by default on HTML
# generated sites, while natively working in PDF
# output, also.
#
# Overwrites visit_reference() Sphinx method found
# in HTMLTranslator class of sphinx/sphinx/writers/html.py
# Solution Source: https://stackoverflow.com/a/61669375/5340149
class PatchedHTMLTranslator(HTMLTranslator):
    def visit_reference(self, node: Element) -> None:
        atts = {"class": "reference"}
        if node.get("internal") or "refuri" not in node:
            atts["class"] += " internal"
        else:
            atts["class"] += " external"
            # Customize behavior (open in new tab, secure linking site)
            atts["target"] = "_blank"
            atts["rel"] = "noopener noreferrer"
        if "refuri" in node:
            atts["href"] = node["refuri"] or "#"
            if self.settings.cloak_email_addresses and atts["href"].startswith(
                "mailto:"
            ):
                atts["href"] = self.cloak_mailto(atts["href"])
                self.in_mailto = True
        else:
            assert (
                "refid" in node
            ), 'References must have "refuri" or "refid" attribute.'
            atts["href"] = "#" + node["refid"]
        if not isinstance(node.parent, nodes.TextElement):
            assert len(node) == 1 and isinstance(node[0], nodes.image)
            atts["class"] += " image-reference"
        if "reftitle" in node:
            atts["title"] = node["reftitle"]
        if "target" in node:
            atts["target"] = node["target"]
        self.body.append(self.starttag(node, "a", "", **atts))

        if node.get("secnumber"):
            self.body.append(
                ("%s" + self.secnumber_suffix) % ".".join(map(str, node["secnumber"]))
            )


# Run above custom function against links
def setup(app):
    app.set_translator("html", PatchedHTMLTranslator)


this_year = datetime.datetime.today().year
copyright_year = f"2022 - {this_year}"

# -- Project information -----------------------------------------------------

project = "Salt install guide"
copyright = f"{copyright_year}, VMware, Inc."
author = "VMware, Inc."

# Variables to pass into the docs from sitevars.txt for rst substitution
with open("sitevars.rst") as site_vars_file:
    site_vars = site_vars_file.read().splitlines()

rst_prolog = """
{}
""".format(
    "\n".join(site_vars[:])
)

# Pull release from "release" in sitevars.rst
release = [s for s in site_vars if "|minor-lts-version|" in s][0].split(":: ")[1]
version = release

# Grab major version for URL version selector generation
current_version = version.split(".")[0]

##
# Furo theme version selector setup
##
# Pull from JSON in GitLab Snippet
"""
supported_versions_json = requests.get(
    "https://gitlab.com/saltstack/open/docs/salt-install-guide/-/snippets/2580440/raw/main/supported-versions.json"
)
supported_versions = supported_versions_json.json()
supported_major_versions = [
    full_version.split(".")[0]
    for full_version in supported_versions["supported_versions"]
]
supported_major_versions.sort()

# Build out version menu
latest_version = supported_versions["latest_version"].split(".")[0]
versions = supported_major_versions
url_prefix = "https://docs.saltproject.io/salt/install-guide/en/"
html_context = make_html_context(
    url_prefix=url_prefix,
    current_version=current_version,
    latest_version=latest_version,
    versions=versions,
)
"""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# HEY, SALT PROJECT MEMBERS! If you add a new extension, help us keep this list
# alphabetized. Also, make sure you add the extension to all the docs repos
# using this toolchain to keep us consistent. Thanks in advance!

extensions = [
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.todo",
    "sphinx-prompt",  # Required by sphinx_substitution_extensions
    "sphinx_inline_tabs",
    "sphinx_substitution_extensions",
]
# Render TODO directives
todo_include_todos = True

source_suffix = ".rst"

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "sitevars.rst",
    "topics/_includes/*.rst",
    "_templates/*.rst",
]


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Base Furo Theme requirements
# More: https://pradyunsg.me/furo/customisation/
html_show_sourcelink = True  # False on private repos; True on public repos
html_theme = "furo"
html_title = "Salt install guide"

html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": "#66CCF4",
        "color-brand-content": "#66CCF4",
    },
    "announcement": '<font color="orange"><strong>IMPORTANT ANNOUNCEMENT:</strong> repo.saltproject.io has migrated to packages.broadcom.com!<br /><strong><a href="https://saltproject.io/blog/salt-install-guide-overhaul/" target="_blank" rel="noopener noreferrer">Click here for latest update (2024-10-31)</a></strong></font>',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://example.com)
html_css_files = [
    "css/announcement-sticky.css",
    "css/import-all-salt-docs.css",
    "css/local-testing.css",
]

copybutton_selector = "div:not(.no-copybutton) > div.highlight > pre"

# Sphinx Multiversion options
# smv_branch_whitelist = r'^30.*$'
# smv_latest_version = "3005"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# For example, official Salt Project docs use images from the salt-branding-guide
# https://gitlab.com/saltstack/open/salt-branding-guide/
#
# Example for >=4.0.0 of Sphinx (support for favicon via URL)
# html_logo = "https://gitlab.com/saltstack/open/salt-branding-guide/-/raw/master/logos/SaltProject_altlogo_teal.png"
# Example for <4.0.0 of Sphinx, if added into _static/img/ and html_static_path is valid
html_logo = "_static/img/SaltProject_altlogo_blue.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large. Favicons can be up to at least 228x228. PNG
# format is supported as well, not just .ico'
# For example, official Salt Project docs use images from the salt-branding-guide
# https://gitlab.com/saltstack/open/salt-branding-guide/
#
# Example for >=4.0.0 of Sphinx (support for favicon via URL)
# html_favicon = "https://gitlab.com/saltstack/open/salt-branding-guide/-/raw/master/logos/SaltProject_Logomark_teal.png"
# Example for <4.0.0 of Sphinx, if added into _static/img/ and html_static_path is valid
html_favicon = "_static/img/SaltProject_Logomark_teal.png"

###
# PDF Generation / LaTeX configuration
###
# If generating PDFs in the future, should ensure external logo is copied local
# https://gitlab.com/saltstack/open/salt-branding-guide/-/raw/master/logos/SaltProject_altlogo_teal.png?inline=true
# latex_logo = "docs/_static/img/SaltProject_verticallogo_black.png"

# Linux Biolinum, Linux Libertine: https://en.wikipedia.org/wiki/Linux_Libertine
# Source Code Pro: https://github.com/adobe-fonts/source-code-pro/releases
latex_elements = {
    "inputenc": "",
    "utf8extra": "",
    "preamble": r"""
    \usepackage{fontspec}
    \setsansfont{Linux Biolinum O}
    \setromanfont{Linux Libertine O}
    \setmonofont{Source Code Pro}
""",
}

suppress_warnings = ["autosectionlabel.*"]
