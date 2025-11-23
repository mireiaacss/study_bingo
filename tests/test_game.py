# tests/test_game.py

import sys
import os
import importlib
from unittest.mock import patch
import pytest

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import board  


def import_game():
    with patch("builtins.input", return_value="1"):
        if "game" in sys.modules:
            del sys.modules["game"]
        return importlib.import_module("game")


def test_choose_subject():
    game = import_game()

    fake_files = ["git_docker.csv", "terminal_bash.csv"]

    with patch.object(game.os, "listdir", return_value=fake_files), \
         patch.object(game.os.path, "isfile", return_value=True), \
         patch("builtins.input", return_value="2"):

        path = game.choose_subject()

    assert path == os.path.join("data/", "terminal_bash.csv")


def test_pair_questions_answers():
    game = import_game()

    def fake_give_questions(csv_path):
        return ["Q1", "Q2", "Q3"]

    def fake_give_answers(csv_path):
        return ["A1", "A2"]

    with patch.object(game, "give_questions", fake_give_questions), \
         patch.object(game, "give_answers", fake_give_answers):

        pairs = game.pair_questions_answers("fake.csv")

    assert len(pairs) == 2
    assert set(pairs) == {("Q1", "A1"), ("Q2", "A2")}


def test_find_answer_position():
    game = import_game()

    card = [
        ["A1", "A2"],
        ["A3", "A4"],
    ]

    assert game.find_answer_position(card, "A3") == (1, 0)
    assert game.find_answer_position(card, "HELLO") is None


def test_print_error_log(capsys):
    game = import_game()

    errors = [
        ("Q1", "A1", "X"),
        ("Q2", "A2", "Y"),
    ]

    game.print_error_log(errors)
    output_non_empty = capsys.readouterr().out

    assert "MISTAKES SUMMARY" in output_non_empty
    assert "Q1" in output_non_empty
    assert "A1" in output_non_empty
    assert "X" in output_non_empty

    game.print_error_log([])
    output_empty = capsys.readouterr().out
    assert output_empty == ""


def test_play_round(capsys):
    game = import_game()

    def fake_pairs(csv):
        return [("Q1", "A1")]

    def fake_board(csv):
        return [
            [f"A{r}_{c}" for c in range(board.COLS)]
            for r in range(board.ROWS)
        ]

    with patch.object(game, "pair_questions_answers", fake_pairs), \
         patch.object(game, "generate_bingo_card", fake_board), \
         patch.object(game, "ask_for_coord_or_skip", return_value=None):

        result = game.play_round()

    out = capsys.readouterr().out
    assert "goodbye" in out.lower()
    assert result is None


def test_main(capsys):
    game = import_game()

    with patch.object(game, "play_round", return_value=False):
        game.main()

    out = capsys.readouterr().out
    assert "Do you want to play again?" not in out
