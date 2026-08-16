#!/usr/bin/env python3

"""
Tests for vtclear.
"""

import io
import sys

import pytest

from vtclear import CLEAR_SCREEN
from vtclear import clear_screen


class RecordingStream(io.StringIO):
    """
    Stream that records everything written so far on each flush() call.
    """

    def __init__(self) -> None:
        super().__init__()
        self.flushes: list[str] = []

    def flush(self) -> None:
        self.flushes.append(self.getvalue())


def test_clear_screen_constant() -> None:
    """
    The escape sequence is erase-display followed by cursor-home.
    """
    assert CLEAR_SCREEN == "\x1b[2J\x1b[H"


def test_clear_screen_writes_the_escape_sequence(
    capsys: pytest.CaptureFixture[str]
) -> None:
    """
    Nothing but the escape sequence is written: no trailing newline.
    """
    clear_screen()

    assert capsys.readouterr().out == CLEAR_SCREEN


def test_clear_screen_flushes_stdout(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    The sequence has no newline, so a line buffered stdout would hold it
    back until some later write. It must be flushed on the spot.
    """
    stream = RecordingStream()
    monkeypatch.setattr(sys, "stdout", stream)

    clear_screen()

    assert stream.flushes == [CLEAR_SCREEN]
