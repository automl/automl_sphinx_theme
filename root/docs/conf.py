import sys, os
sys.path.insert(0, os.path.abspath('../'))

import src
import src.package1.file1
import automl_sphinx_theme


CUSTOM_OPTIONS = {
    'html_theme_options': {
        'github_url': 'https://renesass.de'
    }
}


# Import conf.py from the automl theme
automl_sphinx_theme.set_options(
    globals(),
    src,
    CUSTOM_OPTIONS
)
