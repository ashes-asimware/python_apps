import tkinter as tk
import math


class CatAndMouse:
    def __init__(self, root):
        self.root = root
        self.root.title("Cat and Mouse")

        # Configure the main window size
        self.root.geometry("400x400")

        # Create the CAT label with emoji
        self.cat = tk.Label(
            self.root,
            text="🐱",
            font=("Segoe UI Emoji", 32),  # Larger font size for emoji
            fg="orange",  # Make it orange like a typical cat
        )
        # Place the CAT in the top-left corner initially
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

        # Bind mouse click event to trigger cat movement
        self.root.bind("<Button-1>", self.on_mouse_click)

        # Use a custom cursor from standard options
        self.root.config(cursor="@" + "🐭" if False else "circle")

    def on_mouse_click(self, event):
        """Handle mouse click to trigger cat movement"""
        # Store the click position
        click_x = event.x
        click_y = event.y
        # Short delay before cat starts moving
        self.root.after(100, lambda: self.move_cat_to_mouse(click_x, click_y))

    def move_cat_to_mouse(self, mouse_x, mouse_y):
        # Calculate the vector from cat to mouse
        dx = mouse_x - self.cat_x
        dy = mouse_y - self.cat_y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance > 10:  # Only move if we're more than 10 pixels away
            # Calculate the new position that maintains 10 pixels distance
            move_ratio = (distance - 10) / distance if distance > 0 else 0

            # Update cat position
            self.cat_x = self.cat_x + dx * move_ratio
            self.cat_y = self.cat_y + dy * move_ratio

            # Update label position with integer coordinates
            self.cat.place(x=int(self.cat_x), y=int(self.cat_y))


if __name__ == "__main__":
    root = tk.Tk()
    app = CatAndMouse(root)
    root.mainloop()
