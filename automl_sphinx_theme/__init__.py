import os
from automl_sphinx_theme.conf import OPTIONS


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return theme_path


def set_options(module, src, custom_options={}):
    OPTIONS["copyright"] = src.copyright
    OPTIONS["author"] = src.author
    OPTIONS["version"] = src.version
    OPTIONS["release"] = src.version
    OPTIONS["project"] = f"{src.name} Documentation"
    OPTIONS["html_theme_path"] = (get_html_theme_path(),)

    for k, v in custom_options.items():
        if isinstance(v, dict):
            if k in OPTIONS:
                OPTIONS[k].update(v)
                continue

        OPTIONS[k] = v

    for k, v in OPTIONS.items():
        module[k] = v


def setup(app):
    theme_path = get_html_theme_path()
    app.add_html_theme("automl_sphinx_theme", theme_path)

    # Read the Docs uses ``readthedocs`` as the name of the build, and also
    # uses a special "dirhtml" builder so we need to replace these both with
    # our custom HTML builder
    from automl_sphinx_theme.translator import BootstrapHTML5Translator

    app.set_translator("html", BootstrapHTML5Translator)
    app.set_translator("readthedocs", BootstrapHTML5Translator, override=True)
    app.set_translator("readthedocsdirhtml", BootstrapHTML5Translator, override=True)

    from automl_sphinx_theme.layout import (
        update_config,
        setup_edit_url,
        add_toctree_functions,
        update_templates,
    )

    app.connect("env-updated", update_config)
    app.connect("html-page-context", setup_edit_url)
    app.connect("html-page-context", add_toctree_functions)
    app.connect("html-page-context", update_templates)

    # Update templates for sidebar
    pkg_dir = os.path.abspath(os.path.dirname(__file__))
    path_templates = os.path.join(pkg_dir, "templates")
    app.config.templates_path.append(path_templates)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
