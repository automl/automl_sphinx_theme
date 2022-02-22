
# AutoML Sphinx Theme

The goal of this repository is to set up a documentation as fast and as clean as possible. In your
source project you only need to install `automl_sphinx_theme` to get all the features you need.
Those include automatic API generation, beautiful theme, numpy docstring interpretation, and
executing/plotting examples.

<b>NO COMPLICATED `.conf` OR SPHINX KNOWLEDGE ARE NECESSARY!</b><br />
:sparkling_heart: You're welcome. :sparkling_heart:


## Installation

- Include `name`, `version`, `author`, `copyright` in `{PACKAGE_NAME}/__init__.py`.
- Copy the `docs` and `examples` directories to your root folder. You don't have to include all
files but you should at least include `docs/conf.py` and `docs/Makefile`.
- In `docs/conf.py` change `src` to `{PACKAGE_NAME}`. Adapt the file if needed.
- Install this repo via pypi:
```
pip install automl_sphinx_theme
```
- You can generate the docs via `make html` inside the docs directory. Have a look inside the
`Makefile` to get more information and commands.

We recommend using the repository `automl_template` which incorporates `automl_sphinx_theme`
automatically.


## Github

The documentation can be pushed automatically to a branch, which is used to display a webpage.
Follow the steps to enable it:
- Copy `.github/workflows/docs.yml` to you root folder.
- Create a new branch called `gh-pages`.
- Go to `settings > pages` and select `gh-pages` as source.


## Customization

- Logo: Add docs/images/logo.png.
- Favicon: Add docs/images/favicon.ico.