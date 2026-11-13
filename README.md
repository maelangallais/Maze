# 🧩 Maze

A collection of procedural **Maze Generation** and **Pathfinding** scripts written in MicroPython for the **NumWorks** calculator.

---

## 📂 Scripts Included

```
Maze/
├── maze_solver.py   # Procedural maze generator + fast A* / pathfinding solver
├── maze_v1.py       # Interactive maze game (map-based generation)
└── maze_v2.py       # Optimized maze game designed for smaller grids & PC/calculator compatibility
```

---

### 1. `maze_solver.py` *(Created August 16, 2024)*
- Generates a full-screen procedural maze (`320 × 222` pixels) and solves it automatically.
- Typically resolves even the largest calculator-scale mazes in **under 0.5 seconds**.

### 2. `maze_v1.py` *(Created March 25, 2024)*
- Interactive maze generation and exploration game using an in-memory map grid.
- Includes an in-game startup menu explaining all controls and rules.

### 3. `maze_v2.py` *(Created May 16, 2025)*
- Reworked interactive maze variant tailored for compact, challenging mazes on the calculator.
- Draws directly to the screen and is optimized to run smoothly across both physical NumWorks hardware and PC emulators.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `ion`, `random`, `time`).
