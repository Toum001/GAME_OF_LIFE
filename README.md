# Conway's Game of Life

Personal project by Zo_Toum

Conway's Game of Life is a simulation of the famous cellular automaton created by John Conway, built in Python with Pygame. Each cell lives or dies based on the state of its neighbors, creating dynamic patterns that evolve over generations.

## ✨ Description

This project allows you to:
- visualize a living grid in real time,
- manually modify the state of cells,
- start or pause the simulation,
- reset the grid to test new patterns.

## 📜 Rules

The rules of the Game of Life are:
- a live cell with 2 or 3 neighbors stays alive,
- a live cell with fewer than 2 neighbors dies,
- a live cell with more than 3 neighbors dies,
- a dead cell with exactly 3 neighbors becomes alive.

## ▶️ Controls

- Space: start / pause the simulation
- Left click: toggle a cell on or off
- C: reset the grid
- Escape: quit the game

## 🧩 Project structure

- `main.py`: main game loop, event handling, and display management
- `life.py`: Game of Life logic (`create_map`, `count_around`, `next_generation`)
- `display.py`: drawing of the grid and cells on the Pygame window

## 🚀 Installation

Make sure Python is installed, then install the required dependency:

```bash
pip install pygame
```

## ▶️ Run the project

From the project folder:

```bash
python main.py
```

## 🧠 Example of use

When the program starts, all cells are dead. You can then:
1. click on cells to create your own pattern,
2. press space to start the simulation,
3. observe the evolution of the cells from one generation to the next.

## 👤 Author

Zo_Toum

## 📝 Note

This is my first project in Python.

This is a small personal project designed to explore cellular automata logic and get familiar with Pygame.
