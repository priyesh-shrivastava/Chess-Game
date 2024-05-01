## File Contents

This repository contains the following files and directories:

- `main.py`: The entry point of the chess game application.
             It initializes the game and handles user interactions.

- `chess_ai/`: This directory contains the AI logic for the chess game.
    - `__init__.py`: Makes the directory a Python package.
    - `ai_engine.py`: Contains the AI algorithm that powers the game's medium difficulty setting.
    - `evaluation.py`: Includes the evaluation functions the AI uses to make decisions.

- `chess_engine/`: This directory holds the core game logic.
    - `__init__.py`: Makes the directory a Python package.
    - `board.py`: Defines the chessboard and keeps track of the game state.
    - `pieces.py`: Contains classes for each type of chess piece with their respective moves and rules.

- `ui/`: This directory is responsible for the game's user interface.
    - `__init__.py`: Makes the directory a Python package.
    - `console_ui.py`: A console-based user interface for playing the game.
    - `graphics_ui.py`: (Optional) A graphical user interface, if implemented.

- `tests/`: Contains unit tests to ensure the game and AI are functioning correctly.
    - `test_chess_engine.py`: Tests for the core game logic.
    - `test_chess_ai.py`: Tests for the AI's decision-making capabilities.

- `requirements.txt`: Lists all the Python dependencies required to run the game.

- `LICENSE`: The license file for the project.

- `.gitignore`: Specifies intentionally untracked files to ignore.

Feel free to explore the files and contribute to the development of this intelligent chess game!
