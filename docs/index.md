# Study Bingo

Overview
- Study Bingo is a trivia-based bingo game. Each cell contains an answer.
- Players mark the cell that corresponds to the answer of the given question.

Game Rules
- A card is a rectangular grid (default 3x9).
- The system draws questions one at a time.
- If the answer to the question appears on your card, type the cell position. If the answer to the question is not on your card, type n.
.
- A player can declare "BINGO" to claim a win. The system verifies if all the cells are marked are correct.

Updating Trivia Content
- Questions live in `data/q&a.csv` with headers: id,question,answer.
- To add or update questions:
  1. Edit `data/q&a.csv`.
  2. Ensure unique `id` values and non-empty `question` and `answer` fields.
  3. Run unit tests: `pytest`

Development Notes
- Core files live in `src/`.
- Tests live in `tests/`.
- Configurable settings are in `src/config/settings.yaml`.


