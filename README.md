# SPACESHIP ESCAPADE

## Group Members

| Name | UID |
|--------|--------|
| Ta Nam Trung | 3036690045 |
| Aarav Sinha | 3036684436 |
| Ayana Oner | 3036751174 |
| Suhani Aggarwal | 3036684785 |

---

## Game Description

SPACESHIP ESCAPADE is a single-player terminal-based puzzle adventure game.

The player takes the role of John, an astronaut trapped inside a malfunctioning spaceship. To reach the control room and escape before the spacecraft fails, the player must solve a sequence of interconnected puzzles. Each puzzle provides clues, hints, or codes that are required to progress through the game.

The game combines logical reasoning, pattern recognition, and puzzle-solving skills in a multi-stage escape-room experience.

---

## Game Objectives

The player must:

1. Solve the Wordle puzzle and unlock Chest 1.
2. Solve the Reactor Core puzzle and unlock Chest 2.
3. Use clues from both chests to identify the correct escape door.
4. Complete the Labyrinth puzzle and unlock Chest 3.
5. Decode the final clues and discover the secret word.
6. Escape the spaceship successfully.

---

## Game Features

- Interactive terminal-based gameplay.
- Three unique puzzle types.
- Colour-coded user interface using ANSI escape codes.
- Notebook system for storing clues and hints.
- Interconnected puzzle progression.
- Multiple failure conditions.
- Final code-breaking challenge.

---

## Project Structure

| File | Description |
|--------|--------|
|Suhani.py | Main game flow and puzzle integration |
| Trung.py | Wordle puzzle |
| Aarav.py | Reactor Core puzzle |
| Ayana.py | Labyrinth puzzle |

---

## Puzzle Overview

### Chest 1 – Wordle Puzzle

The player must guess a randomly selected six-letter word within six attempts.

Features:
- Random word selection
- Coloured feedback system
- Input validation
- Bonus hint for successful completion

---

### Chest 2 – Reactor Core Puzzle

The player must stabilise a reactor grid by managing node energy levels.

Features:
- Grid-based gameplay
- Thermal and Electric node mechanics
- Chain reaction behaviour
- Strategic resource management

---

### Chest 3 – Labyrinth Puzzle

The player navigates a maze while avoiding an enemy.

Features:
- Real-time enemy pursuit
- Key collection system
- Multiple maze layouts
- Exit unlocking mechanic

---

## Technical Concepts Used

This project demonstrates:

- Modular programming
- Functions and function decomposition
- Lists and nested data structures
- Conditional statements
- Iteration and loops
- Input validation
- Randomisation
- State tracking
- String processing
- Terminal graphics and ANSI colouring

---

## Running the Game

Start the Docker container:

```bash
docker run -it main
```

Once inside the container, run:

```bash
python main.py
```

The game requires:
- Python 3
- A terminal size of at least 80 × 24

If the terminal is smaller than the required size, the game will pause and prompt the user to resize the terminal before continuing.

## Testing

The following scenarios were tested:

- Valid and invalid menu selections
- Winning and losing Wordle
- Winning and losing Reactor Core
- Winning and losing Labyrinth
- Incorrect chest codes
- Incorrect door selection
- Incorrect final secret word
- Notebook functionality
- Full game completion

---

## Known Limitations

- ANSI colours may not display correctly in some terminals.
- The game requires a terminal size of at least 80 × 24.
- Restarting the game requires rerunning the program.
- Word lists and maze layouts are predefined.
- Enemy movement uses a simple pursuit strategy and does not perform advanced pathfinding.

---

## Contributions

### Ta Nam Trung
- Designed and implemented the Wordle puzzle
- Integrated puzzle modules into the main game
- Implemented game progression and clue system

### Aarav Sinha
- Designed and implemented the Reactor Core puzzle
- Balanced puzzle mechanics
- Edited the project trailer

### Ayana Oner
- Designed and implemented the Labyrinth puzzle
- Created maze layouts and enemy behaviour
- Edited the demonstration video

### Suhani Aggarwal
- Designed and implemented the escape-room system
- Assisted with overall game integration
- Tested and refined gameplay flow

---

## References

- Python Documentation
- ANSI Escape Code Reference

---

## Declaration

This project was developed solely by the group members listed above.
