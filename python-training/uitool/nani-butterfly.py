import tkinter as tk
import math


class CatAndMouse:
    def __init__(self, root):
        self.root = root
        self.root.title("Nani's Garden")
        # Configure the main window size
        self.root.geometry("400x400")

        # Create a canvas with grassy background
        self.canvas = tk.Canvas(
            self.root,
            width=400,
            height=400,
            bg="#90EE90",  # Light green color
            highlightthickness=0,
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create grass texture using overlapping ovals for a knoll effect
        # Draw rolling hills
        self.canvas.create_oval(-50, 300, 200, 450, fill="#7CCD7C", outline="")
        self.canvas.create_oval(150, 320, 450, 480, fill="#87CEEB", outline="")
        self.canvas.create_oval(100, 280, 350, 420, fill="#98FB98", outline="")
        self.canvas.create_oval(250, 310, 500, 460, fill="#90EE90", outline="")

        # Add some grass blades for texture
        for i in range(50):
            import random

            x = random.randint(0, 400)
            y = random.randint(250, 400)
            self.canvas.create_line(
                x,
                y,
                x + random.randint(-2, 2),
                y - random.randint(5, 15),
                fill="#228B22",
                width=1,
            )

        # Create a canvas widget for the little girl
        self.girl_canvas = tk.Canvas(
            self.canvas, width=50, height=60, bg="#90EE90", highlightthickness=0, bd=0
        )

        # Draw the little girl on the canvas
        self.draw_girl(self.girl_canvas)

        # Store reference to the girl canvas
        self.cat = self.girl_canvas

        # Place the girl in the top-left corner initially
        self.cat.place(x=0, y=0)

        # Initialize positions
        self.cat_x = 0
        self.cat_y = 0
        self.last_mouse_x = 0
        self.last_mouse_y = 0

        # Ensure the window is fully created and positioned
        self.root.update_idletasks()

        # Force CAT to be visible at initial position
        self.cat.place(x=self.cat_x, y=self.cat_y)

        # Configure window to show in center of screen
        window_width = 400
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create butterfly cursor (50% smaller: 24 -> 12)
        self.butterfly_cursor = tk.Label(
            self.canvas, text="🦋", font=("Segoe UI Emoji", 12), bg="#90EE90"
        )
        self.butterfly_cursor.place_forget()

        # Make butterfly cursor non-interactive (pass through clicks)
        self.butterfly_cursor.bind("<Button-1>", self.on_mouse_click)

        # Bind mouse events
        self.canvas.bind("<Motion>", self.update_butterfly_cursor)
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        self.canvas.bind("<Leave>", self.hide_butterfly_cursor)

        # Hide default cursor
        self.canvas.config(cursor="none")

    def draw_girl(self, canvas):
        """Draw a little girl on the given canvas"""
        # Draw hair (brown)
        canvas.create_oval(12, 3, 38, 22, fill="#8B4513", outline="#654321")

        # Draw head (peach/skin tone)
        canvas.create_oval(15, 8, 35, 28, fill="#FFD5B5", outline="#D2A679")

        # Draw eyes
        canvas.create_oval(19, 15, 23, 19, fill="black")
        canvas.create_oval(27, 15, 31, 19, fill="black")

        # Draw smile
        canvas.create_arc(
            20,
            18,
            30,
            25,
            start=200,
            extent=140,
            style="arc",
            width=2,
            outline="#D2691E",
        )

        # Draw dress (pink)
        canvas.create_polygon(
            15, 28, 35, 28, 40, 52, 10, 52, fill="#FFB6C1", outline="#FF69B4", width=2
        )

        # Draw arms (skin tone)
        canvas.create_line(15, 32, 5, 42, fill="#FFD5B5", width=4, capstyle="round")
        canvas.create_line(35, 32, 45, 42, fill="#FFD5B5", width=4, capstyle="round")

        # Draw legs (skin tone)
        canvas.create_rectangle(18, 52, 22, 58, fill="#FFD5B5", outline="")
        canvas.create_rectangle(28, 52, 32, 58, fill="#FFD5B5", outline="")

        # Draw shoes (red)
        canvas.create_oval(16, 57, 24, 61, fill="red", outline="darkred")
        canvas.create_oval(26, 57, 34, 61, fill="red", outline="darkred")

    def update_butterfly_cursor(self, event):
        """Update butterfly cursor position"""
        self.butterfly_cursor.place(x=event.x - 6, y=event.y - 6)
        self.butterfly_cursor.lift()

    def hide_butterfly_cursor(self, event):
        """Hide butterfly cursor when leaving canvas"""
        self.butterfly_cursor.place_forget()

    def on_mouse_click(self, event):
        """Handle mouse click to trigger girl movement"""
        # Get the actual canvas coordinates
        if event.widget == self.butterfly_cursor:
            # Click was on the butterfly, translate to canvas coordinates
            click_x = event.x + int(self.butterfly_cursor.place_info()["x"])
            click_y = event.y + int(self.butterfly_cursor.place_info()["y"])
        else:
            # Click was directly on canvas
            click_x = event.x
            click_y = event.y

        # print(f"Click detected at: x={click_x}, y={click_y}")
        # print(f"Girl current position: x={self.cat_x}, y={self.cat_y}")

        # Calculate distance and direction
        dx = click_x - self.cat_x
        dy = click_y - self.cat_y
        distance = math.sqrt(dx * dx + dy * dy)

        # Move girl to within 25 pixels of the butterfly
        if distance > 10:
            move_ratio = (distance - 25) / distance
            self.cat_x = self.cat_x + dx * move_ratio
            self.cat_y = self.cat_y + dy * move_ratio
        else:
            self.cat_x = click_x
            self.cat_y = click_y

        # print(f"Girl new position: x={self.cat_x}, y={self.cat_y}")

        # Update girl position
        self.cat.place(x=int(self.cat_x), y=int(self.cat_y))
        self.cat.update()  # Force immediate update
        # print(f"Girl placed at: x={int(self.cat_x)}, y={int(self.cat_y)}")
        # print("---")


if __name__ == "__main__":
    root = tk.Tk()
    app = CatAndMouse(root)
    root.mainloop()
