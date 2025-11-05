# src/board.py 
import random
import questions

def generate_bingo_card(csv_path):
    """Generate a 3x9 bingo card filled with random answers from the CSV."""
    answers = questions.take_dataset(csv_path)
    chosen = random.sample(answers, 27)  # 3 x 9 = 27 answers
    card = [chosen[i*9:(i+1)*9] for i in range(3)]
    return card


def print_bingo_card(card):
    """Print the board with coordinates (A - I, 1 - 3)."""
    column_labels = [' A  ',' B ',' C ',' D ',' E ',' F ',' G ',' H ',' I ']
    cell_width = 15
    print("\n    " + "".join(label.center(cell_width + 3) for label in column_labels))
    print("   " + ("-" * (cell_width + 3) * len(column_labels)))
    #print("\n   " + "  ".join(column_labels))
    #print("  " + "-----" * len(column_labels))
    #for i, row in enumerate(card, start=1):
        #formatted_row = " | ".join(cell[:10].center(10) for cell in row)
        #print(f"{i} | {formatted_row}")
    for i, row in enumerate(card, start=1):
        formatted_row = " | ".join(cell[:cell_width].center(cell_width) for cell in row)
        print(f"{i} | {formatted_row}")
        print("   " + ("-" * (cell_width + 3) * len(column_labels)))


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



if __name__ == "__main__":
    path = "data/q&a.csv"
    card = generate_bingo_card(path)
    print_bingo_card(card)
