import os
import warnings
from automl_sphinx_theme.conf import OPTIONS

DEFAULT_THEME = {"github_url": "https://automl.github.io/automl_sphinx_theme/main"}


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return theme_path


def set_options(module, options=None):

    if options is not None:
        if "html_theme_options" not in options:
            options["html_theme_options"] = DEFAULT_THEME

        for k, v in options.items():
            if isinstance(v, dict) and k in OPTIONS:
                OPTIONS[k].update(v)
            else:
                OPTIONS[k] = v

    required_params = {"copyright", "author", "version", "name"}
    missing = required_params - set(OPTIONS.keys())

    if len(missing) > 0:
        replace_str = "FIXME"
        warnings.warn(
            "automl_sphinx_theme.set_options(options={...}) is missing keys."
            f" Using '{replace_str}' for options: \n\t{missing}."
        )
        OPTIONS.update({key: replace_str for key in missing})

    OPTIONS["release"] = OPTIONS["version"]
    OPTIONS["project"] = f"{OPTIONS['name']} Documentation"
    OPTIONS["html_theme_path"] = [get_html_theme_path()]

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
