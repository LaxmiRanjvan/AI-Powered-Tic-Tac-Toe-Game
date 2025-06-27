import tkinter as tk
from tkinter import messagebox
import time

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.attributes('-fullscreen', True)  # Enable full-screen mode
        self.window.bind("<Escape>", lambda e: self.window.attributes('-fullscreen', False))
        self.window.configure(bg='#A2B5CD')
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        frame = tk.Frame(self.window, bg='#A2B5CD')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        tk.Label(frame, text="Tic Tac Toe", font=("Arial", 32, "bold"), bg='#A2B5CD').pack(pady=20)
        tk.Button(frame, text="Play with AI", command=self.play_with_ai, width=25, height=2, font=("Arial", 16)).pack(pady=10)
        tk.Button(frame, text="Two Player", command=self.two_player, width=25, height=2, font=("Arial", 16)).pack(pady=10)
        tk.Button(frame, text="Exit", command=self.window.quit, width=25, height=2, font=("Arial", 16)).pack(pady=10)

    def play_with_ai(self):
        self.clear_window()
        frame = tk.Frame(self.window, bg='#A2B5CD')
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        tk.Label(frame, text="Choose X or O", bg='#A2B5CD', font=("Arial", 24, "bold")).pack()
        tk.Button(frame, text="X", command=lambda: self.start_game('X', 'AI'), width=10, height=2, font=("Arial", 16)).pack(pady=10)
        tk.Button(frame, text="O", command=lambda: self.start_game('O', 'AI'), width=10, height=2, font=("Arial", 16)).pack(pady=10)
        tk.Button(frame, text="Back", command=self.main_menu, width=15, height=2, font=("Arial", 16)).pack(pady=10)

    def two_player(self):
        self.start_game('X', 'Player')

    def start_game(self, player_symbol, mode):
        self.clear_window()
        self.board = [' ' for _ in range(9)]
        self.current_turn = 'X'
        self.player_symbol = player_symbol
        self.mode = mode
        self.buttons = []
        
        game_frame = tk.Frame(self.window, bg='#A2B5CD')
        game_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        
        for row in range(3):
            for col in range(3):
                btn = tk.Button(game_frame, text='', font=('Arial', 36), width=6, height=3,
                                command=lambda r=row, c=col: self.on_click(r, c))
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(btn)
        
        self.turn_label = tk.Label(self.window, text=f"{self.current_turn} Turn", font=('Arial', 20, "bold"), bg='#A2B5CD')
        self.turn_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        
        btn_frame = tk.Frame(self.window, bg='#A2B5CD')
        btn_frame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        tk.Button(btn_frame, text="Restart", command=self.reset_board, font=("Arial", 16), width=12).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Back", 
          command=self.main_menu if mode == 'Player' else self.play_with_ai, 
          font=("Arial", 16), width=12).pack(side=tk.RIGHT, padx=10)


        if self.mode == 'AI' and self.current_turn != self.player_symbol:
            self.ai_move()

    def reset_board(self):
        for i in range(9):
            self.board[i] = ' '
            self.buttons[i].config(text='')

        self.current_turn = 'X'
        self.turn_label.config(text=f"{self.current_turn} Turn")

        if self.mode == 'AI' and self.current_turn != self.player_symbol:
            self.ai_move()

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == ' ':
            self.board[index] = self.current_turn
            self.buttons[index].config(text=self.current_turn)
            winner = self.check_winner()

            if winner or ' ' not in self.board:
                self.window.update()
                time.sleep(1)
                self.show_game_result(winner)
                return

            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            self.turn_label.config(text=f"{self.current_turn} Turn")

            if self.mode == 'AI' and self.current_turn != self.player_symbol:
                self.ai_move()

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.current_turn
                score = self.minimax(False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.on_click(best_move // 3, best_move % 3)

    def minimax(self, is_maximizing):
        winner = self.check_winner()
        if winner == self.player_symbol:
            return -1
        elif winner == ('O' if self.player_symbol == 'X' else 'X'):
            return 1
        elif ' ' not in self.board:
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = ('O' if self.player_symbol == 'X' else 'X')
                    score = self.minimax(False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.player_symbol
                    score = self.minimax(True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]
        return None

    def show_game_result(self, winner):
        result_text = f"{winner} wins!" if winner else "It's a tie!"
        messagebox.showinfo("Game Over", result_text)
        self.reset_board()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToe().run()
