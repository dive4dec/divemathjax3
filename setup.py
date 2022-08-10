"""
divemathjax3 setup
"""
import setuptools
import json
from pathlib import Path

try:
    from jupyter_packaging import (
        wrap_installers,
        npm_builder,
        get_data_files,
    )


    HERE = Path(__file__).parent.resolve()

    # The name of the project
    name = "divemathjax3"

    lab_path = (HERE / name / "labextension")

    # Representative files that should exist after a successful build
    jstargets = [
        str(lab_path / "package.json"),
    ]

    labext_name = "divemathjax3"

    data_files_spec = [
        ("share/jupyter/labextensions/%s" % labext_name, str(lab_path), "**"),
        ("share/jupyter/labextensions/%s" % labext_name, str(HERE), "install.json"),
    ]

    cmdclass = wrap_installers(
            post_develop=npm_builder(path=HERE, build_cmd='build:prod', npm=["jlpm"]), 
            ensured_targets=jstargets
    )

    # js_command = combine_commands(
    #     install_npm(HERE, build_cmd="build:prod", npm=["jlpm"]),
    #     ensure_targets(jstargets),
    # )

    # if (HERE / "PKG-INFO").exists():
    #     # In an extracted python source package
    #     cmdclass["jsdeps"] = skip_if_exists(jstargets, js_command)
    # else:
    #     cmdclass["jsdeps"] = js_command

    # Get the package info from package.json
    pkg_json = json.loads((HERE / "package.json").read_bytes())

    setup_args = dict(
        version=pkg_json["version"],
        url=pkg_json["homepage"],
        author=pkg_json["author"]["name"],
        author_email=pkg_json["author"]["email"],
        description=pkg_json["description"],
        license=pkg_json["license"],
        cmdclass=cmdclass,
        data_files = get_data_files(data_files_spec),
        zip_safe=False,
        include_package_data=True,
        python_requires=">=3.6",
    )
except ImportError:
    setup_args = {}

if __name__ == "__main__":
    setuptools.setup(**setup_args)
