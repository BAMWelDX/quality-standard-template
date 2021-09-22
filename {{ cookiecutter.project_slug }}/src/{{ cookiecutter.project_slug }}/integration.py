import sys
from pathlib import Path

from weldx.config import QualityStandard

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources

import {{ cookiecutter.project_slug }}
from asdf.resource import DirectoryResourceMapping


def get_quality_standard():
    resources_root = importlib_resources.files({{ cookiecutter.project_slug}}) / "resources"
    if not resources_root.is_dir():
        # In an editable install, the resources directory will exist off the
        # repository root:
        resources_root = Path(__file__).parent.parent.parent / "resources"
        if not resources_root.is_dir():
            raise RuntimeError("Missing resources directory")

    return QualityStandard(resources_root / "{{ cookiecutter.organization_name }}")
