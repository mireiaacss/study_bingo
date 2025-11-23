# tests/test_questions.py

import sys
import os
import pytest

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import questions  


def create_sample_csv(tmp_path):
    csv_path = tmp_path / "sample_git.csv"

    csv_content = (
        "question;answer\n"
        "How do you initialize a new Git repository?;git init\n"
        "How do you check your Git version?;git --version\n"
        "How do you clone a remote repository?;git clone\n"
    )

    csv_path.write_text(csv_content, encoding="utf-8")
    return csv_path


def test_give_answers(tmp_path):
    csv_path = create_sample_csv(tmp_path)

    answers = questions.give_answers(str(csv_path))

    assert answers == [
        "git init",
        "git --version",
        "git clone",
    ]


def test_give_questions(tmp_path):
    csv_path = create_sample_csv(tmp_path)

    qs = questions.give_questions(str(csv_path))

    assert qs == [
        "How do you initialize a new Git repository?",
        "How do you check your Git version?",
        "How do you clone a remote repository?",
    ]
