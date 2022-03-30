# Python SSSD LDAP Auth

_A Python package which supports deobfuscating LDAP passwords
contained in (System Security Services Daemon) sssd.conf files._

## Inspiration

- [Michael Ludvig](https://github.com/mludvig)'s [sss_deobfuscate](https://github.com/mludvig/sss_deobfuscate) script.
- [SSSD](https://github.com/SSSD/sssd)'s [/src/util/crypto/libcrypto/crypto_obfuscate.c](https://github.com/SSSD/sssd/blob/master/src/util/crypto/libcrypto/crypto_obfuscate.c) source file.

## Features

- Type Hints / Editor Completion
- Readable
- Fully Tested
- Python 3.6 - 3.10 Support

## Install

```sh
$ pip install sssdldapauth
```

## Usage

```python
from sssdldapauth import deobfuscate

password = deobfuscate("<obfuscated_password>")
```

## Development

### Required Software

Refer to the links provided below to install these development dependencies:

- [direnv](https://direnv.net)
- [git](https://git-scm.com/)
- [pyenv](https://github.com/pyenv/pyenv#installation)

### Getting Started

**Setup**

```sh
$ <runtimes.txt xargs -n 1 pyenv install -s
$ direnv allow
$ pip install -r requirements/dev.txt
$ pre-commit install
$ pip install -e .
```

**Tests**

_Run the test suite against the active python environment._

```sh
$ pytest
```

_Run the test suite against the active python environment and watch the codebase
for any changes._

```sh
$ ptw
```

_Run the test suite against all supported python versions._

```sh
$ tox
```

### Publishing

**Create**

1. Update the version number in `sssdldapauth/__init__.py`.

2. Add an entry in `HISTORY.md`.

3. Commit the changes, tag the commit, and push the tags:

   ```sh
   $ git commit -am "v<major>.<minor>.<patch>"
   $ git tag v<major>.<minor>.<patch>
   $ git push origin main --tags
   ```

4. Convert the tag to a release in GitHub with the history entry as the
   description.

**Build**

```sh
$ python -m build
```

**Upload**

```
$ twine upload dist/*
```
