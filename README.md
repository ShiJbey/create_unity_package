# Create Unity Package

<p align="center">
  <img src="https://img.shields.io/pypi/dm/create-unity-package">
  <img src="https://img.shields.io/pypi/l/create-unity-package">
  <img src="https://img.shields.io/pypi/v/create-unity-package">
</p>

This is a simple command line tool that automates the creation of
Unity packages. It creates the boilerplate package structure and
inserts user-specific information. This package is inspired by
other developer CLI tools such as CreateReactApp.

This application follows the instructions offered by
[Unity](https://docs.unity3d.com/Manual/CustomPackages.html). It
creates new local packages in the directory that the application
is run.

Good luck with your development!

## Usage

### How to install

**Option #1**: Install from Pip: `pip install create_unity_package`

**Option #2**: Install from GitHub: `pip install git+https://github.com/ShiJbey/create_unity_package.git`

### How to create a new Unity Package

Run the following command and answer the prompts: `python -m create_unity_package`

### How to import and edit package in Unity

Unity has detailed instructions for developing a local package.
You can instructions for installing a local package
[here](https://docs.unity3d.com/Manual/upm-ui-local.html).

Now you should see the your package name in the `Packages` directory
in Unity's file explorer.
