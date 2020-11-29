#!/usr/bin/env python
from setuptools import setup, find_packages


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
    use_scm_version=True,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
)
