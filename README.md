# VSCode Setup #

### Required Extensions ###
- :link: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- :link: [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

### VSCode Settings ###

```json
{
    "python.languageServer": "Pylance",
    "python.analysis.extraPaths": [
        <site-packages>,
        <pimoroni-pico-stubs>
    ],
}
```

Replace `<site-packages>` with the output of the following command
```bash
python3 -m site --user-site
```

`<pimoroni-pico-stubs>` is the download location of this repo

### Micropython stubs ###

To get micropython type hints you'll need to install the following package:

#### pico ####
```
pip install micropython-rp2-pico-stubs
```

#### pico-w ####
```
pip install micropython-rp2-pico-w-stubs
```

### Standard libaries ###

Micropython and Python standard libraries sometimes differ and by default the type hints will use the standard library over micropython. In order to get micropython type hints instead import the `u` prefixed library e.g.
```python
import utime as time
```
