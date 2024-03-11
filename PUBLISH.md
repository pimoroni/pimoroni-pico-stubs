# Publishing

Publishing is done using poetry, so it should be installed.

Requirements:

- poetry installed and on path
  `pip install -r requirements.txt`
- poetry api key stored in systems secure store or in environment variable `PYPI_API_KEY`

## One time setup ( per host / environment)
### PYPI test

- add repository to poetry config
  `poetry config repositories.test-pypi https://test.pypi.org/legacy/`

- get token from https://test.pypi.org/manage/account/token/
- store token using `poetry config pypi-token.test-pypi pypi-YYYYYYYY`
  Note: 'test-pypi' is the name of the repository

### PyPI Production

- get token from https://pypi.org/manage/account/token/
- store token using `poetry config pypi-token.pypi pypi-XXXXXXXX`

## Bump Version

`poetry version prerelease`
`poetry version patch`

## Poetry Publish

To test:

- `poetry publish -r test-pypi`

To PyPI:

- `poetry publish --build`
