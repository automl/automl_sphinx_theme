import os
import automl_sphinx_theme


OPTIONS = {
    "extensions": [
        "sphinx.ext.autodoc",
        "sphinx.ext.viewcode",
        "sphinx.ext.napoleon",  # Enables to understand NumPy docstring
        # "numpydoc",
        "sphinx.ext.autosummary",
        "sphinx.ext.autosectionlabel",
        "sphinx_autodoc_typehints",
        "sphinx_gallery.gen_gallery",
        # 'sphinx.ext.coverage',
        # 'sphinx.ext.mathjax',
        # 'sphinx.ext.viewcode',
        # 'sphinx.ext.autosummary',
        # "sphinx.ext.autosectionlabel",
        # "sphinx.ext.autodoc",
        # "sphinx.ext.doctest",
        # "sphinx.ext.napoleon",
        # "sphinx_gallery.gen_gallery",
        # "sphinx.ext.autosectionlabel",
        # "sphinx.ext.autodoc",
        # "sphinx.ext.doctest",
    ],
    "suppress_warnings": [
        "autosectionlabel.*",
    ],
    "autosummary_generate": True,
    # "napoleon_google_docstring": True,
    "napoleon_numpy_docstring": True,
    "napoleon_include_init_with_doc": False,
    "napoleon_include_private_with_doc": False,
    "napoleon_include_special_with_doc": True,
    # "napoleon_use_admonition_for_examples": False,
    # "napoleon_use_admonition_for_notes": False,
    # "napoleon_use_admonition_for_references": False,
    # "napoleon_use_ivar": False,
    # "napoleon_use_param": True,
    # "napoleon_use_rtype": True,
    # "napoleon_preprocess_types": False,
    # "napoleon_type_aliases": None,
    # "napoleon_attr_annotations": True,
    "autosectionlabel_maxdepth": 1,
    # Add any paths that contain templates here, relative to this directory.
    "templates_path": [
        "templates",
        os.path.join(str(automl_sphinx_theme.__path__), "templates"),
    ],
    # The suffix(es) of source filenames.
    # You can specify multiple suffix as a list of string:
    # source_suffix": ['.rst', '.md']
    "source_suffix": ".rst",
    # The master toctree document.
    "master_doc": "index",
    "language": None,
    # List of patterns, relative to source directory, that match files and
    # directories to ignore when looking for source files.
    "exclude_patterns": ["static", "templates"],
    # The name of the Pygments (syntax highlighting) style to use.
    "pygments_style": None,  # "sphinx",
    "html_theme": "automl_sphinx_theme",
    "html_logo": "images/logo.png",
    "html_favicon": "images/favicon.ico",
    "autodoc_default_options": {
        "members": True,
        "methods": True,
        "special-members": "__call__",
        "exclude-members": "_abc_impl",
        "show-inheritance": True,
    },
    "sphinx_gallery_conf": {
        # path to the examples
        "examples_dirs": "../examples",
        "gallery_dirs": "examples",
        "show_signature": "False",
        "show_memory": "False",
        "plot_gallery": "True",
        "ignore_pattern": ".*pcs$|__init__\\.py$",
    },
}
