from typing import Optional, Tuple
from board import COLS, ROWS

possible_cols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
possible_rows = "123456789"
VALID_COLS = str(possible_cols[0: COLS])  # COLS columns
VALID_ROWS = str(possible_rows[0: ROWS])        # ROWS rows

def coord_to_indices(coord: str) -> Optional[Tuple[int, int]]:
    """
    Convert a coordinate like 'B2' (or 'b2') into zero-based indices (row, col).
    Return None if the format is invalid or out of range.
    """
    if not coord:
        return None

    coord = coord.strip().upper().replace(" ", "")
    if len(coord) < 2:
        return None

    col_letter = coord[0]
    row_part = coord[1:]
    if col_letter not in VALID_COLS or not row_part.isdigit():
        return None

    row_num = int(row_part)
    if str(row_num) not in VALID_ROWS:
        return None

    col_idx = VALID_COLS.index(col_letter)
    row_idx = row_num - 1
    return (row_idx, col_idx)


def ask_for_coord_or_skip(
    prompt: str = "Enter coordinate (e.g. B2), ENTER to skip if the answer is not in your board, or 'q' to quit: "
) -> Optional[str]:
    """
    Ask the player for input:
      - returns '' (empty string) if player presses ENTER to skip,
      - returns normalized coordinate like 'B2' if valid,
      - returns None if player wants to quit.
    Keeps asking until it gets '', a valid coordinate, or a quit token.
    """
    while True:
        raw = input(prompt)
        if raw.strip().lower() in {"q", "quit", "exit"}:
            return None
        if raw.strip() == "":
            return ""  # skip

        idx = coord_to_indices(raw)
        if idx is not None:
            r, c = idx
            return "ABCDEFGHI"[c] + str(