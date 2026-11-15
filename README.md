# SPACESHIP ESCAPADE

## Team Members and Contributions

| Name | UID | Contribution |
|--------|--------|--------|
| Ta Nam Trung | 3036690045 | Designed and implemented the Wordle puzzle, integrated game modules, and developed the clue and notebook systems.|
| Aarav Sinha | 3036684436 | Designed and implemented the Reactor Core puzzle, balanced reactor mechanics, edited the trailer |
| Ayana Oner | 3036751174 | Designed and implemented the Labyrinth puzzle, created enemy movement logic, edited the demonstration video |
| Suhani Aggarwal | 3036684785 | Designed and implemented the Escape Room section, integrated game components, tested gameplay flow |

---

# Game Objective and Concept

SPACESHIP ESCAPADE is a single-player terminal-based puzzle adventure game.

The player takes the role of John, an astronaut trapped inside a malfunctioning spaceship. To reach the control room and escape before the spacecraft fails, the player must solve a sequence of connected puzzles. Each puzzle rewards the player with clues, codes, or hints that are needed to progress through later stages of the game.

The game combines logical reasoning, code breaking, pattern recognition, and problem-solving in a multi-stage escape room experience.

To win, the player must:

1. Solve the Wordle puzzle and unlock Chest 1.
2. Solve the Reactor Core puzzle and unlock Chest 2.
3. Use clues from both chests to identify the correct escape door.
4. Complete the Labyrinth puzzle and unlock Chest 3.
5. Decode the final clues and discover the secret word.
6. Escape the spaceship successfully.

---

# How to Run the Game

Inside the Docker container, run:

```bash
python main.py
```

Requirements:

- Python 3
- Terminal size of at least 80 × 24

If the terminal window is smaller than 80 × 24, the game will pause and ask the player to resize the terminal before continuing.

---

# How the Game Works

## Main Room

At the start of the game, the player is placed inside an escape room containing two puzzle chests and multiple doors.

### Commands

| Command | Action |
|----------|----------|
| 1 | Move to Chest 1 |
| 2 | Move to Chest 2 |
| N | Open the notebook |

The notebook stores discovered codes, clues, and hints.

The player may solve Chest 1 or Chest 2 first.

---

## Chest 1 – Wordle Puzzle

The first puzzle is a Wordle-style word guessing game.

### Rules

- The player must guess a secret six-letter word.
- The player has six attempts.
- A random word is selected from a predefined word list.

### Colour Feedback

- Green = correct letter in the correct position.
- Yellow = correct letter in the wrong position.
- Gray = letter does not appear in the word.

### Reward

Upon completion, the player receives:

- Chest code: `B@D!`
- Bonus hint (if the puzzle is successfully solved)

This chest also provides a clue needed later to identify the correct door.

---

## Chest 2 – Reactor Core Puzzle

The second puzzle requires the player to stabilise a reactor grid.

### Rules

- The reactor contains 25 nodes.
- Every node must have an energy level between 1 and 5.
- Thermal nodes and Electric nodes affect neighbouring cells differently.
- The puzzle must be completed within the move limit.

### Commands

| Command | Action |
|----------|----------|
| A1 – E5 | Charge a node |
| HINT | Display a hint |
| QUIT | Leave the puzzle |

### Reward

Upon completion, the player receives:

- Chest code: `A_J4`
- Bonus hint (if successfully solved)

This chest also provides a second clue needed to identify the correct escape door.

---

## Escape Door

After opening both chests, the player must combine their clues.

The clues identify which numbered door leads to freedom.

Choosing an incorrect door results in a game over.

---

## Chest 3 – Labyrinth Puzzle

After escaping the first room, the player enters a second area containing a maze challenge.

### Controls

| Key | Action |
|------|------|
| W | Move Up |
| A | Move Left |
| S | Move Down |
| D | Move Right |
| Q | Quit |

### Objective

- Find and collect the key.
- Avoid the enemy.
- Reach the exit.

### Reward

Upon completion, the player receives:

- Chest code: `A0RU`
- Bonus hint (if successfully solved)

---

## Final Escape Challenge

After opening Chest 3, the player receives the final coded clues.

The player must decode the symbols:

```
E19
C1
P5
```

to determine the final secret word.

Entering the correct secret word unlocks the victory door and completes the game.

---

# Imported Modules

## Standard Python Modules

| Module | Purpose |
|----------|----------|
| os | Screen clearing and terminal operations |
| random | Random word and maze selection |
| sys | Program termination |
| time | Typing effects and animations |
| shutil | Terminal size detection |

## Custom Modules

| Module | Purpose |
|----------|----------|
| Trung.py | Wordle puzzle |
| Aarav.py | Reactor Core puzzle |
| Ayana.py | Labyrinth puzzle |

---

# Technical Features

This project demonstrates:

- Modular programming
- Function decomposition
- Lists and nested data structures
- Conditional logic
- Iteration and loops
- Input validation
- Randomisation
- Grid-based game logic
- State tracking
- ANSI terminal colouring
- Multi-stage puzzle progression

---

# Testing

The following scenarios were tested:

### Gameplay Tests

- Complete game completion
- Opening chests in different orders
- Correct final escape sequence

### Error Handling Tests

- Invalid menu commands
- Invalid Wordle guesses
- Invalid reactor coordinates
- Invalid maze commands
- Incorrect chest codes
- Incorrect door selections
- Incorrect final secret word

### Puzzle Tests

- Winning Wordle
- Losing Wordle
- Winning Reactor Core
- Losing Reactor Core
- Winning Labyrinth
- Losing Labyrinth
- Notebook functionality

---

# Known Limitations

- The game requires a terminal size of at least 80 × 24.
- ANSI colours may not display correctly in some terminals.
- Restarting the game requires running the program again.
- Word lists and maze layouts are predefined.
- Enemy movement uses a simple pursuit algorithm rather than advanced pathfinding.
- The game is designed for keyboard input and terminal environments only.

---

# References

- Python Documentation
- ANSI Escape Code Reference

---

# Declaration

All source code, puzzle designs, terminal artwork, and gameplay mechanics were developed by the team members listed above.
