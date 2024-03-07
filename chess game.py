# import os
# import sys
# import chess
# import chess.svg

# def display_board(board):
#     print(chess.svg.board(board=board, lastmove=None, check=None, coordinates=True))

# def get_move():
#     move = input("Enter your move (e.g. e2e4): ")
#     try:
#         move = chess.Move.from_uci(move)
#         if move in board.legal_moves:
#             return move
#         else:
#             print("Illegal move. Try again.")
#             return get_move()
#     except ValueError:
#         print("Invalid input. Try again.")
#         return get_move()

# def main():
#     board = chess.Board()
#     while not board.is_game_over():
#         display_board(board)
#         move = get_move()
#         board.push(move)
#         os.system('cls' if os.name == 'nt' else 'clear')
#     print("Game over.")
#     print(board.result())

# if __name__ == "__main__":
#     main()

















import tkinter as tk
from tkinter import messagebox

# Create a board with alternating colors
def create_board():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            if (i + j) % 2 == 0:
                row.append('#F0D9B5')
            else:
                row.append('#B58863')
        board.append(row)
    return board

# Create a list of piece images
def create_piece_images():
    piece_images = []
    for piece in ['WR', 'WN', 'WB', 'WQ', 'WK', 'WP', 'BR', 'BN', 'BB', 'BQ', 'BK', 'BP']:
        if piece[0] == 'W':
            piece_images.append(tk.PhotoImage(file=f'white_{piece[1:]}.png'))
        else:
            piece_images.append(tk.PhotoImage(file=f'black_{piece[1:]}.png'))
    return piece_images

# Initialize the board and pieces
board = create_board()
piece_images = create_piece_images()

# Define the starting positions of the pieces
starting_positions = {
    'WR': (0, 0), 'WN': (1, 0), 'WB': (2, 0), 'WQ': (3, 0), 'WK': (4, 0), 'WP': [(i, 1) for i in range(8)],
    'BR': (0, 7), 'BN': (1, 7), 'BB': (2, 7), 'BQ': (3, 7), 'BK': (4, 7), 'BP': [(i, 6) for i in range(8)]
}

# Create a dictionary to store the pieces on the board
pieces_on_board = {(x, y): piece for piece, (x, y) in starting_positions.items()}

# Create the main window
window = tk.Tk()
window.title("Chess Game")

# Create a frame for the board
board_frame = tk.Frame(window, width=640, height=640, bg='#5C3E17')
board_frame.pack(padx=10, pady=10)

# Create a function to handle clicks on the board
def board_click(event):
    x, y = event.x // 80, event.y // 80
    if (x, y) in pieces_on_board:
        if turn % 2 == 0:
            if pieces_on_board[(x, y)][0] == 'W':
                selected_piece = pieces_on_board[(x, y)]
                valid_moves = get_valid_moves(selected_piece, x, y)
                highlight_squares(valid_moves)
        else:
            if pieces_on_board[(x, y)][0] == 'B':
                selected_piece = pieces_on_board[(x, y)]
                valid_moves = get_valid_moves(selected_piece, x, y)
                highlight_squares(valid_moves)

# Create a function to handle double clicks on the board
def board_double_click(event):
    x, y = event.x // 80, event.y // 80
    if (x, y) in pieces_on_board:
        if turn % 2 == 0:
            if pieces_on_board[(x, y)][0] == 'W':
                selected_piece = pieces_on_board[(x, y)]
                if selected_piece in valid_moves:
                    move_piece(selected_piece, x, y)
                    turn += 1
                    if check_checkmate():
                        messagebox.showinfo("Game Over", "Checkmate!")
                        window.destroy()
                    highlight_squares([])
        else:
            if pieces_on_board[(x, y)][0] == 'B':
                selected_piece = pieces_on_board[(x, y)]
                if selected_piece in valid_moves:
                    move_piece(selected_piece, x, y)
                    turn += 1
                    if check_checkmate():
                        messagebox.showinfo("Game Over", "Checkmate!")
                        window.destroy()
                    highlight_squares([])

# Create a function to get the valid moves for a piece
def get_valid_moves(piece, x, y):
    moves = []
    if piece[1] == 'P':
        moves = pawn_moves(piece[0], x, y)
    elif piece[1] == 'R':
        moves = rook_moves(x, y)
    elif piece[1] == 'N':
        moves = knight_moves(x, y)
    elif piece[1] == 'B':
        moves = bishop_moves(x, y)
    elif piece[1] == 'Q':
        moves = queen_moves(x, y)
    elif piece[1] == 'K':
        moves = king_moves(x, y)
    return moves

# Create a function to move a piece
def move_piece(piece, x, y):
    global pieces_on_board
    piece_to_move = pieces_on_board.pop((x, y))
    pieces_on_board[(x, y)] = '--'
    new_x, new_y = x + piece[1][0], y + piece[1][1]
    pieces_on_board[(new_x, new_y)] = piece_to_move

# Create a function to highlight squares for valid moves
def highlight_squares(moves):
    for move in moves:
        x, y = move
        board[y][x] = '#FF0000'
    board_canvas.delete("highlight")
    board_canvas.create_