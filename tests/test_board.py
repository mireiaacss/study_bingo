import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import board

def test_create_number_dataset_default():
    data = board.create_number_dataset()
    assert data[0] == 1
    assert data[-1] == 99
    assert len(data) == 99


def test_create_number_dataset_custom_range():
    data = board.create_number_dataset(10, 15)
    assert data == [10, 11, 12, 13, 14, 15]


def test_generate_bingo_card_shape():
    card = board.generate_bingo_card()
    assert len(card) == 3
    for row in card:
        assert len(row) == 9


def test_generate_bingo_card_unique_numbers():
    card = board.generate_bingo_card()
    numbers = [n for row in card for n in row]
    assert len(numbers) == len(set(numbers)), "Numbers should be unique"


def test_print_bingo_card_output(capsys):
    card = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24, 25, 26, 27]
    ]
    board.print_bingo_card(card)
    captured = capsys.readouterr()
    assert "A  B  C" in captured.out
    assert "1 |" in captured.out
    assert "3 |" in captured.out
