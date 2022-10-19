import os, sys

sys.path.insert(0, os.path.abspath(".."))

import automl_sphinx_theme  # Must come after the path injection above
from src import copyright, author, version, name


options = {
    "copyright": copyright,
    "author": author,
    "version": version,
    "versions": {
        f"v{version} (stable)": "#",
        "Your custom version here": "#",
    },
    "name": name,
    "html_theme_options": {
        "github_url": "https://github.com/automl/automl_sphinx_theme",
        "twitter_url": "https://twitter.com/automl_org?lang=de",
    },
}

# Import conf.py from the automl theme
automl_sphinx_theme.set_options(globals(), options)
