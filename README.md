# Tic-Tac-Toe (Command-Line Game)

This is a complete, 2-player Tic-Tac-Toe game that runs entirely in the terminal. It was built using object-oriented principles in Python.

This project was created to demonstrate clean code, object-oriented design, and custom exception handling.

---

### Features

* Clean and readable 3x3 game board.
* Turn-based gameplay for 'X' and 'O'.
* Automatic detection of win conditions (horizontal, vertical, and diagonal).
* Automatic detection of a draw (tie game).
* Robust input validation.

---

### Technical Highlights

This project demonstrates proficiency in several key Python concepts:

* **Object-Oriented Programming (OOP):** The entire game logic, state, and behavior are encapsulated within a `TicTacToe` class.
* **Custom Exception Handling:** The program uses custom exceptions (`SquareNotEmptyError` and `SquareNotFoundError`) to manage invalid user moves gracefully instead of crashing.
* **State Management:** The game board and player turns are managed cleanly within the class instance.
* **Algorithmic Logic:** The `game_finished()` method contains the core algorithm for checking all possible win/draw scenarios.

---

### How to Run

1.  Clone this repository or download the `tictactoe.py` file.
2.  Ensure you have Python 3 installed.
3.  Run the game from your terminal:

```bash
python3 tictactoe.py
```

---

### Example Gameplay

----PLATEAU-----
['▢', '▢', '▢']
['▢', '▢', '▢']
['▢', '▢', '▢']
[Joueur X] Choisissez une case :
Horizontal (A,B,C): A
Vertical (1,2,3): 1
----PLATEAU-----
['X', '▢', '▢']
['▢', '▢', '▢']
['▢', '▢', '▢']
[Joueur O] Choisissez une case :
Horizontal (A,B,C): B
Vertical (1,2,3): 2
----PLATEAU-----
['X', '▢', '▢']
['▢', 'O', '▢']
['▢', '▢', '▢']
[Joueur X] Choisissez une case :
Horizontal (A,B,C): A
Vertical (1,2,3): 1
La case A1 est déjà occupée
