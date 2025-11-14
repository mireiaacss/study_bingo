from pathlib import Path
import sys

# Project root = folder that contains "src" and "data"
ROOT_DIR = Path(__file__).resolve().parents[1]

# Make sure Python can find src/questions.py
SRC_DIR = ROOT_DIR / "src"
sys.path.insert(0, str(SRC_DIR))

from questions import give_answers

# Path to your real CSV
CSV_PATH = ROOT_DIR / "data" / "q&a.csv"


def test_answer_1_matches_csv():
    answers = give_answers(str(CSV_PATH))
    # 1st data row in q&a.csv (after header) -> cd ~
    assert answers[0] == "cd ~"


def test_answer_2_matches_csv():
    answers = give_answers(str(CSV_PATH))
    # 2nd data row -> cd ..
    assert answers[1] == "cd .."


def test_answer_3_matches_csv():
    answers = give_answers(str(CSV_PATH))
    # 3rd data row -> cd -
    assert answers[2] == "cd -"


def test_answer_4_matches_csv():
    answers = give_answers(str(CSV_PATH))
    # 4th data row -> cd /
    assert answers[3] == "cd /"


def test_answer_5_matches_csv():
    answers = give_answers(str(CSV_PATH))
    # 5th data row -> rm
    assert answers[4] == "rm"
