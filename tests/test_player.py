# tests/test_player.py

import sys
import os
from unittest.mock import patch
import pytest

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import player  
import board   


def test_coord_to_indices():
    assert player.coord_to_indices("A1") == (0, 0)

    if board.ROWS >= 2 and board.COLS >= 2:
        assert player.coord_to_indices("b2") == (1, 1)

    assert player.coord_to_indices("") is None
    assert player.coord_to_indices("1A") is None
    assert player.coord_to_indices("AA") is None
    assert player.coord_to_indices("A0") is None

    col_too_big = chr(ord("A") + board.COLS) + "1"
    assert player.coord_to_indices(col_too_big) is None

    row_too_big = "A" + str(board.ROWS + 1)
    assert player.coord_to_indices(row_too_big) is None


def test_ask_for_coord_or_skip(capsys):
    with patch("builtins.input", return_value=""):
        result_skip = player.ask_for_coord_or_skip(">")
    assert result_skip == ""

    with patch("builtins.input", return_value="q"):
        result_quit = player.ask_for_coord_or_skip(">")
    assert result_quit is None

    if board.ROWS >= 2 and board.COLS >= 2:
        with patch("builtins.input", return_value="b2"):
            result_coord = player.ask_for_coord_or_skip(">")
        assert result_coord == "B2"

    with patch("builtins.input", side_effect=["Z9", "A1"]):
        result_retry = player.ask_for_coord_or_skip(">")

    assert result_retry == "A1"
