# Study Bingo

Trivia Bingo game where bingo cards contain trivia questions and answers (terminal commands, Python basics and bash).

Installation

1. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

Usage

Run the game:

```bash
python -m src.game..py
```

### Run with Docker Compose

From the project root:

```bash
docker compose run --rm app

###Project structure

```
study_bingo/
├── README.md → Project overview, installation, and instructions for players/developers.
├── requirements.txt → List of Python dependencies to run the project.
├── LICENSE → License for distribution and usage rights.
└── src/
   ├── __init__.py → Marks the folder as a Python package.
   ├── board.py → Functions to generate and manage bingo cards.
   ├── questions.py → Loads and retrieves trivia questions from the CSV.
   ├── player.py → Handles player input and interactions.
   ├── checker.py → Validates answers and checks for BINGO.
   └── game.py → Main game loop, ties together board, player, and checker.
└── tests/
   ├── test_board.py → Tests for card generation logic.
   ├── test_questions.py → Tests for loading and serving trivia questions.
   ├── test_checker.py → Tests for validation and BINGO detection.
   └── test_game.py → Tests for overall game flow.
└── data/
   └── q&a.csv → Trivia question and answer bank used during the game.
└── docs/
   └── index.md → Project documentation (rules, architecture, design notes, or
      usage guide)
```

Contributing

See docs/index.md for rules and guidance on updating trivia content.

# Study Bingo - Sprint 1

## Sprint Goal

Establish the foundation of the Bingo game by setting up the project structure,
creating an initial number dataset, and implementing basic bingo card generation.

## Run locally

pip install -r requirements.txt
python -m src.board

# Study Bingo - Sprint 2

## Sprint Goal

Develop and implement the main features of the Bingo game by drawing
a random number each round, allowing players to mark their cards and validating
their responses in each round and detecting “bingo” when winning.

## Run locally

python src/board.py

python src/questions.py

pytest
