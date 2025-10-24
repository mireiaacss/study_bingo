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
python -m src.game
```

Project structure

- src/: main game package
- data/q&a.csv: question bank
- tests/: unit tests
- docs/: documentation

Contributing

See docs/index.md for rules and guidance on updating trivia content.

