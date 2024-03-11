# Pimoroni Pico MicroPython Stubs

This repository contains type stubs that help you write code for Pimoroni Pico MicroPython's many built-in modules.

Type stubs include details about the constants, functions, classes and methods available in each module, and what arguments they accept.

# VSCode Setup

### Required Extensions

You must install the VSCode Python extension and additionally Pylance to support type hints.

To install extensions, press Ctrl+Shift+P or Cmd+Shift+P and in the pop-up box type "Extensions" and select "Extensions: Install Extensions".

A search box should open on the left-hand side of your editor, find and install the following:

- :link: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- :link: [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

### VSCode Settings

To open VSCode settings press Ctrl+Shift+P or Cmd+Shift+P and in the pop-up box type "Settings" and choose "Preferences: Open Workspace Settings (JSON)".

If the file is empty you can go right ahead and add the lines below:

```json
{
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    },
    "python.analysis.typeshedPaths": [
        "./typings/",
    ],
}

```

### MicroPython stubs

To get MicroPython type hints you'll need to install the following package into the `./typings` directory of your project.

If the terminal is not open press Ctrl+Shift+P or Cmd+Shift+P and in the pop-up box type "Terminal" and select "Terminal: Create New Terminal (In Active Workspace)".

Finally in the terminal run the following command:

```bash
pip install pimoroni-pico-stubs --target ./typings --no-user
```
