import sys, os

sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../src"))

import src
import automl_sphinx_theme


CUSTOM_OPTIONS = {
    "html_theme_options": {
        "github_url": "https://automl.github.io/automl_sphinx_theme/main"
    }
}


# Import conf.py from the automl theme
automl_sphinx_theme.set_options(globals(), src, CUSTOM_OPTIONS)
