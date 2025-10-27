# src/board.py 
import random 
 
def create_number_dataset(start=1, end=99):
    """Return a list of numbers available for the bingo."""
    return list(range(start, end + 1))

def generate_bingo_card():
    """Generate a 3x9 bingo card with random numbers."""
    numbers = create_number_dataset()
    chosen = random.sample(numbers, 27)  # Select 27 unique random numbers
    card = [chosen[i*9:(i+1)*9] for i in range(3)]  # Split into 3 rows of 9
    return card

if __name__ == "__main__":
    card = generate_bingo_card()
    for row in card:
        print(row)