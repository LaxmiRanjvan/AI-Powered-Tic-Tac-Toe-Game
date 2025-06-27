# AI-Powered-Tic-Tac-Toe-Game 🎮

A Python-based **Tic Tac Toe** game with a **Graphical User Interface (GUI)** using **Tkinter** and an **AI opponent** powered by the **Minimax Algorithm**. This project offers both **Player vs Player** and **Player vs AI** modes, ensuring an unbeatable AI experience and smooth gameplay.

---

## 📂 Project Structure
├── TIC_TAC_TOE.PY # Main Python source code

├── Report.pdf # Detailed project report

└── PPT.pdf # Project presentation slides


---

## 🚀 Features

- 🎮 **Two Game Modes:**
  - Player vs Player
  - Player vs AI

- 🤖 **Unbeatable AI:**
  - Implemented using the Minimax algorithm to ensure optimal moves.

- 🖼️ **Graphical User Interface:**
  - Built using Tkinter.
  - Fullscreen experience.
  - Responsive turn indicators and smooth transitions.

- 🔄 **Game Controls:**
  - Restart option.
  - Back to main menu.
  - Exit functionality.

- ✅ **Winner Detection:**
  - Checks rows, columns, and diagonals.
  - Displays result messages (Win, Lose, Tie).

---

## 📌 Technologies Used

- **Programming Language:** Python
- **GUI Library:** Tkinter
- **Algorithm:** Minimax

---

## 🧠 Minimax Algorithm (AI Logic)

The **Minimax Algorithm** is a decision-making strategy used for two-player games like Tic Tac Toe. It systematically evaluates all possible game moves and selects the move that minimizes the potential loss while maximizing potential gain.

In this project:
- The AI simulates **every possible future move**.
- Assigns scores: `+1` if AI wins, `-1` if the player wins, `0` for a draw.
- **Recursively explores** all possibilities until terminal states (win, lose, draw).
- Always selects the move with the highest score to ensure **optimal play**.
- The algorithm guarantees that the AI will never lose if it plays correctly.

---

## 📋 How to Run

1. Make sure Python is installed on your system.
2. Run the game using:
   ```bash
   python TIC_TAC_TOE.PY
   
3. Enjoy playing against another player or the AI!

---

## 🎯 Future Improvements

- Add difficulty levels (Easy, Medium, Hard).

- Support larger grids (4x4, 5x5).

- Introduce timed matches.

- Add custom themes and sound effects.

- Develop mobile and web versions.

---


