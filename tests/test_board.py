# tests/test_board.py

import sys
import os
import csv
import pytest
import yaml

# Add src/ to the import path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import board  


def test_load_settings(tmp_path):
    data = {"ROWS": 3, "COLS": 4}
    yaml_path = tmp_path / "settings.yaml"
    yaml_path.write_text(yaml.safe_dump(data), encoding="utf-8")

    settings = board.load_settings(str(yaml_path))

    assert settings["ROWS"] == 3
    assert settings["COLS"] == 4


def test_generate_bingo_card():
    total_cells = board.ROWS * board.COLS

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    csv_path = os.path.join(base_dir, "data", "git_docker.csv")

    assert os.path.exists(csv_path)

    board.random.seed(0)
    card = board.generate_bingo_card(csv_path)

    assert len(card) == board.ROWS
    assert all(len(row) == board.COLS for row in card)

    flat = [cell for row in card for cell in row]

    assert len(flat) == total_cells
    assert len(flat) == len(set(flat))

    answers = board.questions.give_answers(csv_path)
    assert set(flat).issubset(set(answers))


def test_print_bingo_card(capsys):
    card = [
        [f"R1C{c+1}" for c in range(board.COLS)],
        [f"R2C{c+1}" for c in range(board.COLS)],
    ]

    board.print_bingo_card(card, col_width=8, max_lines=1)
    out = capsys.readouterr().out

    for i in range(board.COLS):
        assert chr(ord("A") + i) in out

    assert "1|" in out
    assert "2|" in out

    assert "R1C1" in out or "R1C2" in out or "R1C3" in out


def test_mark_cell():
    card = [
        ["a", "b"],
        ["c", "d"],
    ]

    board.mark_cell(card, 0, 1)

    assert card[0][1] == "X"
    assert card[0][0] == "a"
    assert card[1][0] == "c"
    assert card[1][1] == "d"


def test_is_complete():
    card = [
        ["X", "X"],
        ["X", "Y"],
    ]

    assert not board.is_complete(card)

    card[1][1] = "X"
    assert board.is_complete(card)

