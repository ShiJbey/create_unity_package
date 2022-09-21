# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4]

### Added

- CLI argument `--git` will initialize the package as a git repo and add
  a `.gitignore` file configured for Unity Packages and C# development
- CLI argument `--verbose` will print logs to the console about the
  application's progress
- `gitignore.txt` template

## [1.0.3]

### Added

- New entry point in setup.cfg so users can run `create-unity-package` without `python -m`

## [1.0.2]

### Added

- New CLI argument "-o, --output" to specify the name of the directory to place the generated package
- New package logo for README

## [1.0.1]

### Fixed

- Jinja2 templates were not getting built into the wheel

## [1.0.0]

- Initial release
