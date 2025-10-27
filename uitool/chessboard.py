import tkinter as tk

class ChessBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Board")
        
        # Add some padding around the board
        self.root.configure(padx=10, pady=10)
        
        # Create the board using Labels
        self.create_board()
        
    def create_board(self):
        """Create the chessboard using Labels in a grid"""
        for row in range(8):
            for col in range(8):
                # Create a label for each square
                square = tk.Label(
                    self.root,
                    width=4,          # Width in text units
                    height=2,         # Height in text units
                    relief="solid",   # Border style
                    borderwidth=1     # Border width
                )
                
                # Set background color (alternating)
                color = "#FFFFFF" if (row + col) % 2 == 0 else "#4A4A4A"
                square.configure(bg=color)
                
                # Place the label in the grid
                square.grid(row=row, column=col, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessBoard(root)
    root.mainloop()
