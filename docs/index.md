# Study Bingo — Documentation

Overview
- Study Bingo is a trivia-based bingo game. Each cell contains a question (and its answer).
- Players mark cells only when they correctly answer the question drawn by the system.

Game Rules (prototype)
- A card is a square grid (default 5x5).
- The center may be a free cell.
- The system draws questions one at a time.
- If the drawn question appears on your card, answer it. If your answer matches the stored answer exactly (case-insensitive), that cell is marked.
- A player can declare "BINGO" to claim a win. The system verifies if a winning pattern is present.
- Winning patterns supported by default:
  - Any complete row
  - Any complete column
  - Either main diagonal

Updating Trivia Content
- Questions live in `data/q&a.csv` with headers: id,question,answer.
- To add or update questions:
  1. Edit `data/q&a.csv`.
  2. Ensure unique `id` values and non-empty `question` and `answer` fields.
  3. Run unit tests: `pytest`

Development Notes
- Core files live in `bingo/`.
- Tests live in `tests/`.
- Configurable settings are in `bingo/config/settings.yaml`.

