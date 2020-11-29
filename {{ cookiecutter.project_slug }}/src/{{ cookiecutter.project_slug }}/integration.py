from pathlib import Path
import sys

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources

from asdf.resource import DirectoryResourceMapping

import {{ cookiecutter.project_slug}}


def get_resource_mappings():
    resources_root = importlib_resources.files({{ cookiecutter.project_slug}}) / "resources"
    if not resources_root.is_dir():
        # In an editable install, the resources directory will exist off the
        # repository root:
        resources_root = Path(__file__).parent.parent.parent / "resources"
        if not resources_root.is_dir():
            raise RuntimeError("Missing resources directory")

    return [
        DirectoryResourceMapping(
            resources_root / "{{ cookiecutter.organization_name }}" / "schemas",
            "{{ cookiecutter.schema_uri_root}}",
        ),
        DirectoryResourceMapping(
            resources_root / "{{ cookiecutter.organization_name }}" / "manifests",
            "{{ cookiecutter.manifest_uri_root}}",
        ),
    ]
