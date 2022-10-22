# rehome

[![Documentation](https://readthedocs.org/projects/rehome/badge/?version=latest)](https://rehome.readthedocs.io/en/latest/)
[![CI Status](https://github.com/lmmx/rehome/actions/workflows/master.yml/badge.svg)](https://github.com/lmmx/rehome/actions/workflows/master.yml)
[![Coverage](https://codecov.io/gh/lmmx/rehome/branch/master/graph/badge.svg)](https://codecov.io/github/lmmx/rehome)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Rehome your Python scripts into nice interconnected modules

[Read The Docs](https://rehome.readthedocs.io/en/latest/)

## Requires

- Python 3.10+

## Installation

```sh
pip install rehome
```

## Usage

The CLI allows you to instantiate the `Rehome` class central to this package directly.

```sh
usage: rehome [-h] [-p [PROTECT ...]] [-g [GROUP ...]] [-d] target

Rehome(target: pathlib.Path, protect: list[str] = <factory>, group: list[str] = <factory>, debug:
bool = False)

positional arguments:
  target

options:
  -h, --help            show this help message and exit
  -p [PROTECT ...], --protect [PROTECT ...]
                        (default: <factory>)
  -g [GROUP ...], --group [GROUP ...]
                        (default: <factory>)
  -d, --debug           (default: False)
```

### Protected names

`-p` specifies names to protect, i.e. to keep in the source file

```sh
rehome foo.py -p main
```

...protects the name `main`, and ensures it will stay in the source file

### Groups

`-g` specifies groups (_each_ argument is a group, separated by spaces)

```sh
rehome foo.py -g "hand glove" "foot sock"
```

...creates two groups of names: `["hand", "glove"]` and `["foot", "sock"]`

> _rehome_ is available from [PyPI](https://pypi.org/project/rehome), and
> the code is on [GitHub](https://github.com/lmmx/rehome)
