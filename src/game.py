import random
from typing import List, Tuple, Optional

from questions import give_questions, give_answers
from board import (
    generate_bingo_card,
    print_bingo_card,
    mark_cell,
    is_complete,
)
from player import ask_for_coord_or_skip, coord_to_indices

CSV_PATH = "data/q&a.csv"   # adjust if needed
MAX_MISTAKES = 3            # lose after 3 mistakes


def pair_questions_answers(csv_path: str) -> List[Tuple[str, str]]:
    """
    Build aligned (question, answer) pairs from the CSV using helper loaders.
    """
    questions = give_questions(csv_path)
    answers = give_answers(csv_path)
    n = min(len(questions), len(answers))
    pairs = list(zip(questions[:n], answers[:n]))
    random.shuffle(pairs)
    return pairs


def find_answer_position(card: List[List[str]], target: str) -> Optional[Tuple[int, int]]:
    """
    Return (row_idx, col_idx) if the answer is on the board, else None.
    """
    for r, row in enumerate(card):
        for c, cell in enumerate(row):
            if cell == target:
                return (r, c)
    return None


def print_error_log(errors: List[Tuple[str, str, str]]) -> None:
    """
    Print errors in the requested format:
    QUESTION - TRUE ANSWER - WRONG ANSWER
    """
    if not errors:
        return
    print("\nERRORS MADE:")
    for q, true_a, wrong_a in errors:

        print(f"{q} - \033[1mThe real answer is:\033[0m {true_a} ✅ - \033[1mbut you answered:\033[0m {wrong_a} ❌")


def main() -> None:
    qa_pairs = pair_questions_answers(CSV_PATH)
    card = generate_bingo_card(CSV_PATH)

    mistakes = 0
    errors: List[Tuple[str, str, str]] = []  # (question, true_answer, wrong_answer_text)

    print("=== STUDY BINGO ===")
    print("Type a coordinate (e.g. B2).")
    print("If you think the answer is NOT on your board, press ENTER to skip.")
    print(f"You lose after {MAX_MISTAKES} mistakes. Type 'q' to quit.\n")

    for question, correct_answer in qa_pairs:
        # Win check at start of round
        if is_complete(card):
            print("\n🎉 BINGO! You completed the board!")
            print_bingo_card(card)
            print_error_log(errors)
            return

        print_bingo_card(card)
        print("\nQuestion:")
        print(f"\n----→ {question}")

        # Check if the correct answer is on the board (for skip penalty logic)
        pos = find_answer_position(card, correct_answer)

        choice = ask_for_coord_or_skip()
        if choice is None:
            print("\nGoodbye!")
            print_error_log(errors)
            return

        # Player pressed ENTER (skip)
        if choice == "":
            # If the answer IS on the board, skipping counts as a mistake
            if pos is not None:
                mistakes += 1
                errors.append((question, correct_answer, "(empty)"))
                #print(f"❌ You skipped a question whose answer was on your board. Mistakes: {mistakes}/{MAX_MISTAKES}\n")
                if mistakes >= MAX_MISTAKES:
                    print("💥 You reached the maximum number of mistakes. You loose.")
                    print_bingo_card(card)
                    print_error_log(errors)
                    return
            else:
                print("\n⏭️  Skipped. Next question.\n")
            continue

        # User entered a coordinate: validate and resolve
        idx = coord_to_indices(choice)  # already validated in ask_for_coord_or_skip, but safe to call
        if idx is None:
            # Defensive: should not happen
            print("⚠️  Invalid coordinate. Turn lost.\n")
            continue

        r, c = idx
        chosen_cell = card[r][c]

        if chosen_cell == correct_answer:
            mark_cell(card, r, c)
            print("✅ Correct! Marked with 'X'.\n")
            if is_complete(card):
                print("\n🎉 BINGO! You completed the board!")
                print_bingo_card(card)
                print_error_log(errors)
                return
        else:
            mistakes += 1
            errors.append((question, correct_answer, chosen_cell))
            #print(f"❌ Wrong cell. Mistakes: {mistakes}/{MAX_MISTAKES}\n")
            if mistakes >= MAX_MISTAKES:
                print("💥 You reached the maximum number of mistakes. You lose.")
                print_bingo_card(card)
                print_error_log(errors)
                return

    # Deck exhausted
    print("\nNo more questions. Game over.")
    print_bingo_card(card)
    if is_complete(card):
        print("🎉 BINGO! (completed exactly at the end)")
    print_error_log(errors)


if __name__ == "__main__":
    main()
