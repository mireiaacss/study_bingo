# Study Bingo

A fully containerized command-line study game implemented in Python.
The application displays questions sourced from a dataset, and player selects answers from a bingo-style board based on coordinates.
The prokect is packaged using Docker to ensure reproductibility and ease of execution on any machine.

## Features

- Bingo board generated automatically from the dataset.
- Randomized question selection.
- Coordinate-based answering mechanism.
- Mistake tracking with loss condition after three incorrect attempts.
- Winning condition when all correct board entries have been crossed out, threshold of errors estbablished at 3.
- Entirely containerized execution without requiring a local Python installation.
- Read-only data volume to maintain dataset integrity.

## Requierements
The game requires only:
- Docker Desktop (macOS, Windows, Linux) or Docker Engine and Docker Compose v2 (Linux)

## Installation

This project is an interactive terminal-based game, so it must be executed in a way that allows Docker to attach a keyboard/TTY to the container.

1. Download the "Docker" folder of the repository.
2. Ensure both Dockerfile and docker-compose.yml are in the same folder.
3. You can verify that Docker and Docker Compose are available:
  ```bash
docker --version
docker compose version
```

## Running the game
Execute the game using:

  ```bash
docker compose run --rm app
```
This command will build the image automatically if it does not exists so only 1 command is needed and not two.
Then, it allocates an interactive terminal required for user input and runs the application.
Once ended, it removes the container upon exist to avoid accumulation of unused containers.
_Note:_
Running the container from Docker Desktop GUI will not work, because the game expects keyboard input.
Docker Desktop does not provide an interactive terminal for input().


## Project structure


```
study_bingo/
├── README.md → Project overview, installation, and instructions for running the game.
├── requirements.txt → List of Python dependencies to run the project.
├── LICENSE → License for distribution and usage rights.
└── src/
   ├── __init__.py → Marks the folder as a Python package.
   ├── board.py → Functions to generate and manage bingo cards.
   ├── questions.py → Loads and retrieves trivia questions from the CSV.
   ├── player.py → Handles player input and interactions.
   └── game.py → Main game loop, ties together board, player, and checker.
└── tests/
   ├── test_board.py → Tests for card generation logic.
   ├── test_questions.py → Tests for loading and serving trivia questions.
   ├── test_checker.py → Tests for validation and BINGO detection.
   └── test_game.py → Tests for overall game flow.
└── data/
   ├── git_docker.csv → Trivia question and answer bank git and docker related used during the game.
   └── terminal_bash.csv → Trivia question and answer bank terminal and bash related used during the game.
└── docs/
   └── index.md → Project documentation (rules, architecture, design notes, or
      usage guide)
└── docker/
   ├── Dockerfile → Builds the game environment by installing Python, adding Git, cloning the repository automatically, installing dependencies, and preparing the application so it can run inside a lightweight container.
   └── docker-compose.yml → Defines how the game container is executed, ensuring the user can run the CLI Bingo game from the terminal with a single command.

```


### Authors

Ana Arroyo, Mireia Calviño, Silvia Carrascosa, Miruna Ghiveci, Maria Fiamenghi, Martina Roig, May Tahri
