# src/board.py 
import random
import questions
from textwrap import wrap
import yaml

def load_settings(yaml_path):
    with open(yaml_path, 'r') as f:
        settings = yaml.safe_load(f)
    return settings

# Usage example
settings = load_settings('src/config/settings.yaml')
ROWS = settings['ROWS']  # load the rows
COLS = settings['COLS']  # load the columns

def generate_bingo_card(csv_path):
    """Generate a ROWSxCOLS bingo card filled with random answers from the CSV."""
    answers = questions.give_answers(csv_path)
    chosen = random.sample(answers, ROWS * COLS)  # total answers
    card = [chosen[i*COLS:(i+1)*COLS] for i in range(ROWS)]
    return card


def print_bingo_card(card, col_width=14, max_lines=2):
    """
    Pretty-print a ROWSxCOLS bingo board.
    - col_width: characters per column (fixed)
    - max_lines: number of wrapped lines per cell
    """
    n_rows, n_cols = len(card), len(card[0])
    assert n_cols == COLS, "Expected COLS columns (A..I)."

    # Column labels A..I
    column_labels = [chr(ord('A') + i) for i in range(n_cols)]
    row_label_w = len(str(n_rows)) + 1  # for '1|', '2|', etc.

    def fmt_cell(text):
        s = str(text).replace("\n", " ")
        lines = wrap(s, width=col_width) or [""]
        # Show all wrapped lines up to max_lines, no ellipsis
        lines = lines[:max_lines]
        while len(lines) < max_lines:
            lines.append("")
        return [line.center(col_width) for line in lines]

    def join_cells(cells):
        return " | ".join(cells)

    # Separator line
    sample_line = join_cells([" " * col_width for _ in range(n_cols)])
    table_width = row_label_w + 2 + len(sample_line)
    hsep = "-" * table_width

    # Header
    header = " " * (row_label_w - 1) + "| " + join_cells(
        [lbl.center(col_width) for lbl in column_labels]
    )
    print("\n" + header)
    print(hsep)

    # Rows
    for r, row in enumerate(card, start=1):
        formatted = [fmt_cell(cell) for cell in row]
        for i in range(max_lines):
            prefix = f"{str(r).rjust(row_label_w-1)}| " if i == 0 else " " * (row_label_w + 1)
            print(prefix + join_cells([formatted[c][i] for c in range(n_cols)]))
        print(hsep)

def mark_cell(card, row, col):
    """Replace a cell with 'X' if correct."""
    card[row][col] = "X"

    


def is_complete(card):
    """Return True if the board is completely marked."""
    for row in card:
        for cell in row:
            if cell != "X":
                return False
    return True

