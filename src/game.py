import random
from typing import List, Tuple, Optional
import os
from questions import give_questions, give_answers
from board import (
    generate_bingo_card,
    print_bingo_card,
    mark_cell,
    is_complete,
)
from player import ask_for_coord_or_skip, coord_to_indices

def choose_subject() -> str:
    data_dir = 'data/'
    available_topics = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    print("Available topics:")
    for idx, subject in enumerate(available_topics, 1):
        print(f"{idx}. {subject}")
    while True:
        try:
            choice = int(input("\nEnter the number of the topic you want to study: "))
            if 1 <= choice <= len(available_topics):
                selected_path = os.path.join(data_dir, available_topics[choice - 1])
                return selected_path
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

CSV_PATH = choose_subject()
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
    print("\n" + "="*30)
    print("❌ MISTAKES SUMMARY ❌")
    print("="*30)
    for q, true_a, wrong_a in errors:
        print(f"❓ Q: {q}")
        print(f"   ✅ Real answer: {true_a}")
        print(f"   ❌ Your answer: {wrong_a}")
        print("-" * 20)


def play_round() -> bool:
    """
    Runs a single game of Bingo.
    Returns True if the game ended naturally (win/loss/empty deck).
    Returns False if the user chose to quit immediately ('q').
    """
        
    qa_pairs = pair_questions_answers(CSV_PATH)
    card = generate_bingo_card(CSV_PATH)

    mistakes = 0
    errors: List[Tuple[str, str, str]] = []   # (question, true_answer, wrong_answer_text)
    correct_log: List[Tuple[str, str]] = []   # (question, correct_answer) - New list for correct ones
    print("\n"*2)
    print("=== STUDY BINGO ===")
    print("Type a coordinate (e.g. B2).")
    print("If you think the answer is NOT on your board, press ENTER to skip.")
    print(f"You loose after {MAX_MISTAKES} mistakes. Type 'q' to quit.\n")

    for question, correct_answer in qa_pairs:
        # Win check at start of round
        if is_complete(card):
            if mistakes == 0:
                print("\n🏆 PERFECT BINGO! You completed the board with no mistakes!")
            else:
                print("\n🎉 BINGO! But you did some mistakes...")
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
                print("\n⏭️  Skipped. Next question.\n")
                if mistakes >= MAX_MISTAKES:
                    print(f"\n💥 GAME OVER! You reached {MAX_MISTAKES} mistakes.")
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

        mark_cell(card, r, c)

        if chosen_cell == correct_answer:
            if is_complete(card):
                print("\n🎉 BINGO! You completed the board!")
                print_bingo_card(card)
                print_error_log(errors)
                return
        else:
            mistakes += 1
            errors.append((question, correct_answer, chosen_cell))
            if mistakes >= MAX_MISTAKES:
                print("💥 You reached the maximum number of mistakes. You lose.")
                print("Here is the list of what went wrong:")
                print_error_log(errors)
                return

    # Deck exhausted
    print("\nNo more questions. Game over.")
    print_bingo_card(card)
    print_error_log(errors)

def main() -> None:
    while True:
        # Runs one game. 
        # result is False ONLY if user typed 'q' to quit the app entirely.
        # result is True if they Won, Lost, or ran out of cards.
        result = play_round()
        
        # If user explicitly typed 'q', we break the loop and close the app.
        if result is False:
            break
        
        # Otherwise (Win or Lose), we ask to play again.
        print("\n" + "-"*40)
        again = input("🔄 Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! See you next time.")
            break
        print("\nRestarting game...\n" + "-"*40 + "\n")


if __name__ == "__main__":
    main()
