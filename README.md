<h1 align="center">
  <img
    width="64"
    height="64"
    src="https://user-images.githubusercontent.com/11076525/190913978-f17fed38-e1d1-4a3c-9547-9d685b9e4a13.png"
  >
  Create Unity Package
</h1>

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

Please file any issues for bugs or desired features.
Good luck with your development!

## Usage

### How to install

**Option #1**: Install from Pip: `pip install create_unity_package`

**Option #2**: Install from GitHub: `pip install git+https://github.com/ShiJbey/create_unity_package.git`

### How to create a new Unity Package

Run the following command in a terminal and answer the prompts: `create-unity-package`

By default, this creates a new folder with the unique package
name entered during the prompts. If you would like to name the
folder differently, you can change the folder name afterward or
use the `--output` argument when generating the package. For more
help use the `--help`.

```
create-unity-package --output <YourPackageName>
```

In your current working directory it will create a new package
directory with the name of your package and the following structure.

```
<root>
  ├── package.json
  ├── README.md
  ├── CHANGELOG.md
  ├── LICENSE.md  # Defaults to MIT License
  ├── Third Party Notices.md
  ├── Editor
  │   ├── [company-name].[package-name].Editor.asmdef
  ├── Runtime
  │   ├── [company-name].[package-name].asmdef
  ├── Tests
  │   ├── Editor
  │   │   ├── [company-name].[package-name].Editor.Tests.asmdef
  │   └── Runtime
  │        ├── [company-name].[package-name].Tests.asmdef
  ├── Samples~
  │        └── [empty]
  └── Documentation~
       └── [package-name].md
```

### How to import and edit package in Unity

Unity has detailed instructions for developing a local package.
You can instructions for installing a local package
[here](https://docs.unity3d.com/Manual/upm-ui-local.html).

Now you should see the your package name in the `Packages` directory
in Unity's file explorer.
