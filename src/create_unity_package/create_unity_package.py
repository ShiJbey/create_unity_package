from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

_TEMPLATES_DIR = Path(os.path.abspath(__file__)).parent / "templates"
_FILE_LOADER = FileSystemLoader(_TEMPLATES_DIR)
_JINJA_ENV = Environment(loader=_FILE_LOADER)


@dataclass
class AuthorInfo:
    name: str
    email: str
    url: str = ''


@dataclass
class PackageInfo:
    name: str
    version: str
    displayName: str
    description: str
    unity: str
    author: AuthorInfo
    keywords: List[str] = field(default_factory=list)


def create_package_json(
    path: Path,
    package_info: PackageInfo
) -> None:
    """
    Create a new package.json file at the given path

    Parameters
    ----------

    """
    output = {
        "name": package_info.name,
        "version": package_info.version,
        "displayName": package_info.displayName,
        "description": package_info.description,
        "unity": package_info.unity,
        "keywords": package_info.keywords,
        "author": {
            "name": package_info.author.name,
            "email": package_info.author.email,
            "url": package_info.author.url
        }
    }

    output_path = path / "package.json"

    with open(output_path, "w") as f:
        f.writelines(json.dumps(output, indent=4))


def create_runtime_assembly_def(path: Path, package_info: PackageInfo) -> None:
    package_name_without_ext = ".".join(package_info.name.split('.')[1:])
    output = {
        "name": f"{package_name_without_ext}.Runtime",
        "references": [],
        "includePlatforms": [],
        "excludePlatforms": [],
        "allowUnsafeCode": False,
        "overrideReferences": False,
        "precompiledReferences": [],
        "autoReferenced": True,
        "defineConstraints": [],
        "versionDefines": [],
        "noEngineReferences": False
    }

    file_name = f"{package_name_without_ext}.Runtime.asmdef"
    output_path = path / file_name

    with open(output_path, "w") as f:
        f.writelines(json.dumps(output, indent=4))


def create_editor_assembly_def(path: Path, package_info: PackageInfo) -> None:
    package_name_without_ext = ".".join(package_info.name.split('.')[1:])
    output = {
        "name": f"{package_name_without_ext}.Editor",
        "references": [
            f"{package_name_without_ext}.Runtime",
        ],
        "includePlatforms": [],
        "excludePlatforms": [],
        "allowUnsafeCode": False,
        "overrideReferences": False,
        "precompiledReferences": [],
        "autoReferenced": True,
        "defineConstraints": [],
        "versionDefines": [],
        "noEngineReferences": False
    }

    file_name = f"{package_name_without_ext}.Editor.asmdef"
    output_path = path / file_name

    with open(output_path, "w") as f:
        f.writelines(json.dumps(output, indent=4))


def create_runtime_tests_assembly_def(path: Path, package_info: PackageInfo) -> None:
    package_name_without_ext = ".".join(package_info.name.split('.')[1:])
    output = {
        "name": f"{package_name_without_ext}.Runtime.Tests",
        "references": [
            f"{package_name_without_ext}.Runtime",
        ],
        "optionalUnityReferences": [
            "TestAssemblies"
        ],
        "includePlatforms": [],
        "excludePlatforms": [],
        "allowUnsafeCode": False,
        "overrideReferences": False,
        "precompiledReferences": [],
        "autoReferenced": True,
        "defineConstraints": [],
        "versionDefines": [],
        "noEngineReferences": False
    }

    file_name = f"{package_name_without_ext}.Runtime.Tests.asmdef"
    output_path = path / file_name

    with open(output_path, "w") as f:
        f.writelines(json.dumps(output, indent=4))


def create_editor_tests_assembly_def(path: Path, package_info: PackageInfo) -> None:
    package_name_without_ext = ".".join(package_info.name.split('.')[1:])
    output = {
        "name": f"{package_name_without_ext}.Editor.Tests",
        "references": [
            f"{package_name_without_ext}.Runtime",
            f"{package_name_without_ext}.Editor"
        ],
        "optionalUnityReferences": [
            "TestAssemblies"
        ],
        "includePlatforms": [],
        "excludePlatforms": [],
        "allowUnsafeCode": False,
        "overrideReferences": False,
        "precompiledReferences": [],
        "autoReferenced": True,
        "defineConstraints": [],
        "versionDefines": [],
        "noEngineReferences": False
    }

    file_name = f"{package_name_without_ext}.Editor.Tests.asmdef"
    output_path = path / file_name

    with open(output_path, "w") as f:
        f.writelines(json.dumps(output, indent=4))


def create_changelog_markdown(path: Path, package_info: PackageInfo) -> None:
    """Creates a new markdown file with package documentation"""
    template = _JINJA_ENV.get_template("changelog.md")
    output = template.render()
    output_path = path / "CHANGELOG.md"

    with open(output_path, 'w') as f:
        f.writelines(output)


def create_license_markdown(path: Path, package_info: PackageInfo) -> None:
    """Creates a new markdown file with package documentation"""
    template = _JINJA_ENV.get_template("license.mit.md")
    output = template.render(
        author_name=package_info.author.name,
        author_email=package_info.author.email
    )
    output_path = path / "LICENSE.md"

    with open(output_path, 'w') as f:
        f.writelines(output)


def create_third_party_notices_markdown(path: Path, package_info: PackageInfo) -> None:
    """Creates a new markdown file with package documentation"""
    output_path = path / "Third Party Notices.md"

    with open(output_path, 'w') as f:
        f.writelines("")


def create_documentation_markdown(path: Path, package_info: PackageInfo) -> None:
    """Creates a new markdown file with package documentation"""

    template = _JINJA_ENV.get_template("package_documentation.md")
    output = template.render(display_name=package_info.displayName)
    output_path = path / f"{package_info.name.split('.')[-1]}.md"

    with open(output_path, 'w') as f:
        f.writelines(output)


def create_package_readme(path: Path, package_info: PackageInfo) -> None:
    """Create a new README markdown file"""

    template = _JINJA_ENV.get_template("readme.template.md")
    output = template.render(display_name=package_info.displayName)
    output_path = path / "README.md"

    with open(output_path, 'w') as f:
        f.writelines(output)


def create_package(package_dir: Path, package_info: PackageInfo) -> None:
    """Create a new package directory and package structure"""
    # Create directory structure
    os.mkdir(package_dir)
    os.mkdir(package_dir / "Documentation~")
    os.mkdir(package_dir / "Samples~")
    os.mkdir(package_dir / "Editor")
    os.mkdir(package_dir / "Runtime")
    os.mkdir(package_dir / "Tests")
    os.mkdir(package_dir / "Tests" / "Editor")
    os.mkdir(package_dir / "Tests" / "Runtime")

    # Create various files
    create_package_json(package_dir, package_info)
    create_package_readme(package_dir, package_info)
    create_third_party_notices_markdown(package_dir, package_info)
    create_license_markdown(package_dir, package_info)
    create_changelog_markdown(package_dir, package_info)
    create_runtime_assembly_def(
        package_dir / "Runtime",
        package_info)
    create_editor_assembly_def(
        package_dir / "Editor",
        package_info)
    create_runtime_tests_assembly_def(
        package_dir / "Tests" / "Runtime",
        package_info)
    create_editor_tests_assembly_def(
        package_dir / "Tests" / "Editor",
        package_info)
    create_documentation_markdown(
        package_dir / "Documentation~",
        package_info)
