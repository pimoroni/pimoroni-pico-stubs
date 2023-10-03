# Pimoroni Pico MicroPython Stubs

This repository contains type stubs that help you write code for Pimoroni Pico MicroPython's many built-in modules.

Type stubs include details about the constants, functions, classes and methods available in each module, and what arguments they accept.

# VSCode Setup

If you're installing these stubs into Visual Studio Code you'll first need to clone this repository onto your computer, or [download the .zip file from the latest release](https://github.com/pimoroni/pimoroni-pico-stubs/releases/latest) or alternatively [find the release that matches the version of Pimoroni Pico MicroPython you're using.](https://github.com/pimoroni/pimoroni-pico-stubs/releases)

To clone the repository, assuming you have git installed:

```
git clone https://github.com/pimoroni/pimoroni-pico-stubs
```

Make a note of the download directory for later:

```
cd pimoroni-pico-stubs
pwd
```

### Required Extensions

You must install the VSCode Python extension and additionally Pylance to support type hints.

To install extensions, press Ctrl+Shift+P or Cmd+Shift+P and in the pop-up box type "Extensions" and select "Extensions: Install Extensions."

A search box should open on the left-hand side of your editor, find and install the following:

- :link: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- :link: [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

### VSCode Settings

To open VSCode settings press Ctrl+Shift+P or Cmd+Shift+P and in the pop-up box type "Settings" and choose "Preferences: Open Workspace Settings (JSON)".

If the file is empty you can go right ahead and add the lines below: 

```json
{
    "python.languageServer": "Pylance",
    "python.analysis.extraPaths": [
        <site-packages>,
        <pimoroni-pico-stubs>/stubs
    ],
}
```

Replace `<site-packages>` with the output of the following command:

```bash
python3 -m site --user-site
```

`<pimoroni-pico-stubs>` is the download location of this repo, which you made a note of earlier.

### MicroPython stubs

To get MicroPython type hints you'll need to install the following package:

#### pico

```
pip install micropython-rp2-pico-stubs
```

#### pico-w

```
pip install micropython-rp2-pico-w-stubs
```

### Standard libaries ###

MicroPython and Python standard libraries sometimes differ and by default the type hints will use the standard library over micropython. In order to get MicroPython type hints instead import the `u` prefixed library e.g:

```python
import utime as time
```
