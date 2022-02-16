import os
from io import open
from automl_sphinx_theme.__version__ import version
from setuptools import setup


def package_files(directory: str):
    """
    Traverses target directory recursivery adding file paths to a list.
    Original solution found at:
        * https://stackoverflow.com/questions/27664504/\
            how-to-add-package-data-recursively-in-python-setup-py

    Parameters
    ----------
    directory: str
        Target directory to traverse.

    Returns
    -------
    paths: list
        List of file paths.
    """

    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))

    return paths


setup(
    name="automl_sphinx_theme",
    version=version,
    url="https://github.com/automl/automl_sphinx_theme",
    license="MIT",
    author="René Sass and Edward Bergman",
    author_email="sass@tnt.uni-hannover.de",
    description="AutoML Theme for Sphinx",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["automl_sphinx_theme"],
    packages=["automl_sphinx_theme"],
    include_package_data=True,
    zip_safe=False,
    package_data={
        "automl_sphinx_theme": [
            "conf.py",
            "layout.py",
            "translator.py",
            "theme.conf",
            "*.html",
            *package_files("automl_sphinx_theme/static"),
            *package_files("automl_sphinx_theme/templates"),
        ]
    },
    entry_points={
        "sphinx.html_themes": [
            "automl_sphinx_theme = automl_sphinx_theme",
        ]
    },
    python_requires=">=3.8",
    install_requires=[
        "sphinx>=4.4.0",
        "sphinx-gallery>=0.10.1",
        "sphinx-toolbox>=2.17.0" "sphinx-autodoc-typehints>=1.16.0",
        "numpydoc>=1.2",
        "beautifulsoup4>=4.10.0",
        "jupyter==1.0.0",
        "notebook>=6.48",
        "matplotlib>=3.5.1",
        "seaborn>=0.11.2",
    ],
    tests_require=[
        "pytest",
    ],
    extras_require={
        "dev": [],
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
