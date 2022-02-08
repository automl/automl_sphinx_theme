from io import open
import os
from os import path
from automl_sphinx_theme import __version__

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
            paths.append(os.path.join('..', path, filename))

    return paths


setup(
    name='automl_sphinx_theme',
    version=__version__,
    url='https://github.com/automl/automl_sphinx_theme',
    license='MIT',
    author='René Sass and Edward Bergman',
    author_email='sass@tnt.uni-hannover.de',
    description='AutoML Theme for Sphinx',
    long_description=open('README.rst', encoding='utf-8').read(),
    py_modules=['automl_sphinx_theme'],
    packages=['automl_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'automl_sphinx_theme': [
        'conf.py',
        'layout.py',
        'translator.py',
        'theme.conf',
        '*.html',
        *package_files('automl_sphinx_theme/static')
    ]},
    entry_points={
        'sphinx.html_themes': [
            'automl_sphinx_theme = automl_sphinx_theme',
        ]
    },
    python_requires='>=3.7',
    install_requires=[
        "sphinx>=4.4.0",
        "sphinx-gallery>=0.10.1",
        "matplotlib>=3.5.1",
        "sphinx-autodoc-typehints>=1.16.0",
        "numpydoc>=1.2"
    ],
    tests_require=[
        'pytest',
    ],
    extras_require={
        'dev': [],
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)