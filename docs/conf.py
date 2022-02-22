import os, sys

sys.path.insert(0, os.path.abspath(".."))

import automl_sphinx_theme  # Must come after the path injection above
from src import copyright, author, version, name


options = {
    "copyright": copyright,
    "author": author,
    "version": version,
    "name": name,
    "html_theme_options": {
        "github_url": "https://automl.github.io/automl_sphinx_theme/main"
        # "twitter_url": "https://twitter.com"
    },
}

# Import conf.py from the automl theme
automl_sphinx_theme.set_options(globals(), options)
