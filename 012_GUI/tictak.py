import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe - Perfect AI")
root.geometry("350x400")
root.resizable(False, False)
root.configure(bg="#F7F7F7")

player = "X"
ai = "O"
board = [""] * 9

wins = [(0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)]

# --- UI update ---
def update_status(msg):
    status_label.config(text=msg)

# --- Win check ---
def check_game_over():
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != "":
            for b in [buttons[i], buttons[j], buttons[k]]:
                b.config(bg="#90ee90")
            messagebox.showinfo("Game Over", f"{board[i]} wins!")
            disable_all()
            return True
    if "" not in board:
        messagebox.showinfo("Game Over", "It's a Draw!")
        return True
    return False

def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

def reset_game():
    global board
    board = [""] * 9
    update_status("Your Turn (X)")
    for i, btn in enumerate(buttons):
        btn.config(text="", bg="white", state="normal")

# --- Player move ---
def player_move(i):
    if board[i] == "":
        board[i] = player
        buttons[i].config(text=player, fg="#333", state="disabled")
        if not check_game_over():
            update_status("System Thinking...")
            root.after(500, ai_move)

# --- AI (Minimax) move ---
def ai_move():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == "":
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        board[best_move] = ai
        buttons[best_move].config(text=ai, fg="red", state="disabled")
        if not check_game_over():
            update_status("Your Turn (X)")

# --- Minimax Algorithm ---
def minimax(state, depth, is_maximizing):
    winner = check_winner(state)
    if winner == ai:
        return 10 - depth
    elif winner == player:
        return depth - 10
    elif "" not in state:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if state[i] == "":
                state[i] = ai
                score = minimax(state, depth+1, False)
                state[i] = ""
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if state[i] == "":
                state[i] = player
                score = minimax(state, depth+1, True)
                state[i] = ""
                best_score = min(best_score, score)
        return best_score

def check_winner(state):
    for i, j, k in wins:
        if state[i] == state[j] == state[k] and state[i] != "":
            return state[i]
    return None

# --- UI Layout ---
status_label = tk.Label(root, text="Your Turn (X)", font=("Arial", 14, "bold"), bg="#F7F7F7", fg="#333")
status_label.pack(pady=10)

frame = tk.Frame(root, bg="#F7F7F7")
frame.pack()

buttons = []
for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 18, "bold"), width=5, height=2, bg="white",
                    command=lambda i=i: player_move(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

tk.Button(root, text="🔄 Reset Game", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=reset_game)\
    .pack(pady=15)

root.mainloop()
