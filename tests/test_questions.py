
import io
import os
from pathlib import Path
import questions

def write_csv(tmp_path, rows):
    p = tmp_path / "qa.csv"
    with open(p, "w", encoding="utf-8", newline="") as f:
        for r in rows:
            # join with semicolon to match the module's expected delimiter
            line = ";".join("" if (x is None) else str(x) for x in r)
            f.write(line + "\n")
    return p

def test_give_answers_reads_second_column_and_skips_header(tmp_path):
    csv_path = write_csv(tmp_path, [
        ("question", "answer"),
        ("Q1", "A1"),
        ("Q2", "A2"),
    ])
    answers = questions.give_answers(csv_path)
    assert answers == ["A1", "A2"]
    # header not present
    assert "answer" not in answers

def test_give_questions_reads_first_column_and_skips_header(tmp_path):
    csv_path = write_csv(tmp_path, [
        ("question", "answer"),
        ("Q1", "A1"),
        ("Q2", "A2"),
    ])
    qs = questions.give_questions(csv_path)
    assert qs == ["Q1", "Q2"]
    assert "question" not in qs

def test_trims_whitespace_and_handles_empty_lines(tmp_path):
    csv_path = write_csv(tmp_path, [
        ("question", "answer"),
        (" Q1  ", "  A1 "),
        ("", ""),           # empty row -> after split, both fields empty strings
        ("Q2", "A2  "),
        ("Q3", ""),         # missing answer (short row handled by implementation condition)
    ])
    answers = questions.give_answers(csv_path)
    questions_list = questions.give_questions(csv_path)
    # give_answers should include trimmed A1, A2, and "" (from the blank row second column)
    assert answers[0] == "A1"
    assert answers[1] == ""    # second column of the blank line
    assert answers[2] == "A2"
    # last row has an empty second column -> included as ""
    assert answers[3] == ""
    # give_questions should include trimmed first column including blank string from empty row
    assert questions_list == ["Q1", "", "Q2", "Q3"]

def test_handles_rows_with_missing_columns(tmp_path):
    # row with only one column after semicolon split should still be accepted for give_questions,
    # but give_answers must skip it because it lacks a second column
    csv_path = write_csv(tmp_path, [
        ("question", "answer"),
        ("OnlyQuestion",),   # one-column row
        ("Q2", "A2"),
    ])
    qs = questions.give_questions(csv_path)
    ans = questions.give_answers(csv_path)
    assert "OnlyQuestion" in qs
    assert "A2" in ans and len(ans) == 1  # the one-column row is ignored by give_answers

def test_supports_utf8_content(tmp_path):
    csv_path = write_csv(tmp_path, [
        ("pregunta", "respuesta"),
        ("¿Capital de España?", "Madrid"),
        ("Área del círculo", "π·r^2"),
        ("Français", "étude"),
        ("Emoji", "✅"),
    ])
    qs = questions.give_questions(csv_path)
    ans = questions.give_answers(csv_path)
    assert "¿Capital de España?" in qs
    assert "π·r^2" in ans
    assert "étude" in ans
    assert "✅" in ans

def test_uses_semicolon_as_delimiter(tmp_path):
    # Mix of commas inside fields should not break since we split on semicolons
    # The answer field contains a comma which should be read as part of the field.
    rows = [
        ("question", "answer"),
        ("Q1 with, comma", "A1 with, comma too"),
        ("Q2", "A2"),
    ]
    # Build file with semicolons, but internal commas inside fields
    csv_path = write_csv(tmp_path, rows)
    qs = questions.give_questions(csv_path)
    ans = questions.give_answers(csv_path)
    assert "Q1 with, comma" in qs
    assert "A1 with, comma too" in ans
