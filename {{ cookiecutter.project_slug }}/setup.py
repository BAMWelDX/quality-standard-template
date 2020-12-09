#!/usr/bin/env python
from setuptools import find_packages, setup
from setuptools_scm import get_version

packages = find_packages(where="src")
packages.append("{{ cookiecutter.project_slug}}.resources")

package_dir = {
    "": "src",
    "{{ cookiecutter.project_slug}}.resources": "resources",
}

package_data = {
    "{{ cookiecutter.project_slug}}.resources": ["*.yaml", "**/*.yaml", "**/**/*.yaml"],
}

setup(
    version=get_version(),
    use_scm_version={
        "write_to": "src/{{ cookiecutter.project_slug }}/_version.py",
        "write_to_template": '__version__ = "{version}"\n',
    },
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
)
