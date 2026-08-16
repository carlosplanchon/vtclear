# vtclear

![vtclear banner](https://raw.githubusercontent.com/carlosplanchon/vtclear/master/assets/banner.jpg)

Python ANSI VT100 implementation of Erase Screen

[![CI](https://github.com/carlosplanchon/vtclear/actions/workflows/ci.yml/badge.svg)](https://github.com/carlosplanchon/vtclear/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/vtclear.svg)](https://pypi.org/project/vtclear/)
[![Python versions](https://img.shields.io/pypi/pyversions/vtclear.svg)](https://pypi.org/project/vtclear/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/carlosplanchon/vtclear)

## installation
```
uv add vtclear
```
or
```
pip install vtclear
```

## usage
```python
from vtclear import clear_screen
clear_screen()
```

The escape sequence itself is exported too, in case you want to write it
somewhere other than stdout:
```python
import sys
from vtclear import CLEAR_SCREEN
sys.stderr.write(CLEAR_SCREEN)
sys.stderr.flush()  # no newline in the sequence, so flush by hand
```

## notes
Any VT100 compatible terminal reads the sequence, Windows Terminal included:
it has been the default host on Windows 11 since 22H2. The exception is the
classic console host, conhost.exe, still the default on Windows 10, where
virtual terminal processing stays off unless something turns it on and CPython
does not. There the sequence is printed verbatim instead of clearing, and
enabling it is the caller's job, e.g. through
`colorama.just_fix_windows_console()`.

## license
This project is licensed under the MIT License.
