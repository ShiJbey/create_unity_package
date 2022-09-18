import sys
import os
from argparse import ArgumentParser, Namespace
from pathlib import Path
import re

import inquirer

import create_unity_package
from create_unity_package.create_unity_package import create_package, PackageInfo, AuthorInfo


def _parse_command_line_args() -> Namespace:
    arg_parser = ArgumentParser(
        prog="Create Unity Package",
        description="Create boilerplate Unity package",
    )

    arg_parser.add_argument(
        "-v", "--version",
        action="store_true",
        default=False,
        help="Print the version of CreateUnityPackage"
    )

    arg_parser.add_argument(
        "-o", "--output",
        type=Path,
        dest="output_path",
        help="the name of the directory to place the generated package"
    )

    return arg_parser.parse_args()


def _prompt_user_for_package_info() -> PackageInfo:
    """
    Prompts the user with questions regarding the package

    Returns
    -------
    PackageInfo:
        Information about the package to create
    """

    questions = [
        inquirer.Text('display_name',
                      message="Package Display Name (publicly visible)"),
        inquirer.Text(
            'unique_package_name', message="Unique Package Name (example com.domain.your_package)"),
        inquirer.Text(
            "version",
            message="Version",
            default="0.0.1"
        ),
        inquirer.Text("description", message="Short Description"),
        inquirer.Text(
            "unity", message="Unity Version (example: 2022.1)", default="2022.1"),
        inquirer.Text("keywords", message="Keywords (separated with comma)"),
        inquirer.Text("author_name", message="Author Name"),
        inquirer.Text("author_email", message="Author Email"),
        inquirer.Text("author_url", message="Author URL"),
    ]

    answers = inquirer.prompt(questions)

    if answers is None:
        sys.exit(1)

    package_name = str(
        answers['unique_package_name']
    ).lower().replace(" ", "")

    if len(package_name) > 214:
        raise ValueError(
            f"package name  ({package_name}) is longer than 214 characters."
        )

    if re.fullmatch(r"[a-z]+.[a-z0-9-_.]+", package_name) is None:
        raise ValueError(
            f"package name  ({package_name}) is not of the form <domain-name-extension>.<company-name>.<package-name>"
        )

    version = str(answers['version'])

    return PackageInfo(
        name=package_name,
        version=version,
        displayName=str(answers['display_name']),
        description=str(answers['description']),
        unity=str(answers['unity']),
        author=AuthorInfo(
            name=str(answers['author_name']),
            email=str(answers['author_email'])
        ),
        keywords=list(
            map(
                lambda s: s.strip(),
                str(answers['keywords']).split(',')
            )
        )
    )


def main():
    args = _parse_command_line_args()

    if args.version:
        print(create_unity_package.__version__)
        sys.exit(0)

    package_info = _prompt_user_for_package_info()

    if args.output_path:
        package_dir = args.output_path
    else:
        package_dir = Path(os.getcwd()) / package_info.name

    create_package(package_dir, package_info)


if __name__ == "__main__":
    main()
