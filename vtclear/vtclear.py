#!/usr/bin/env python3

"""
VT100 ASCII clear implemented in Python.
https://invisible-island.net/xterm/ctlseqs/ctlseqs.html
"""

from typing import Final


#: CSI 2 J (erase the whole display), then CSI H (move the cursor home).
CLEAR_SCREEN: Final[str] = "\x1b[2J\x1b[H"


def clear_screen() -> None:
    """
    Clear the screen.
    """
    print(CLEAR_SCREEN, end="", flush=True)
