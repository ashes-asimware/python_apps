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

        # Create a mouse cursor label
        self.mouse_cursor = tk.Label(
            self.root,
            text="🐭",
            font=("Segoe UI Emoji", 24),
            bg=self.root.cget("bg"),  # Match window background
        )
        self.mouse_cursor.place_forget()  # Hide initially

        # Bind mouse motion event to track cursor
        self.root.bind("<Motion>", self.update_mouse_cursor)
        self.root.bind("<Leave>", self.hide_mouse_cursor)

        # Hide the default cursor when inside the window
        self.root.config(cursor="none")

        # Start periodic check after window is properly positioned
        self.root.after(100, self.start_tracking)

    def start_tracking(self):
        """Start the periodic mouse position checking"""
        self.check_mouse_movement()

    def update_mouse_cursor(self, event):
        """Update the mouse cursor image position"""
        # Position the mouse emoji at the cursor location
        # Offset slightly to center it on the cursor point
        offset_x = -12  # Half of emoji width
        offset_y = -12  # Half of emoji height
        self.mouse_cursor.place(x=event.x + offset_x, y=event.y + offset_y)

    def hide_mouse_cursor(self, event):
        """Hide the mouse cursor when leaving the window"""
        self.mouse_cursor.place_forget()

    def check_mouse_movement(self):
        # Get current mouse position relative to root window
        win_x = self.root.winfo_rootx()
        win_y = self.root.winfo_rooty()
        win_width = self.root.winfo_width()
        win_height = self.root.winfo_height()

        mouse_x = self.root.winfo_pointerx() - win_x
        mouse_y = self.root.winfo_pointery() - win_y

        # Check if mouse is within window bounds
        if 0 <= mouse_x <= win_width and 0 <= mouse_y <= win_height:
            # Check if mouse has moved
            if mouse_x != self.last_mouse_x or mouse_y != self.last_mouse_y:
                self.move_cat_to_mouse(mouse_x, mouse_y)
                self.last_mouse_x = mouse_x
                self.last_mouse_y = mouse_y

        # Schedule next check in 3000ms (3 seconds)
        self.root.after(3000, self.check_mouse_movement)

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
            self.cat.place_forget()  # Remove the previous placement
            self.cat.place(x=int(self.cat_x), y=int(self.cat_y))


if __name__ == "__main__":
    root = tk.Tk()
    app = CatAndMouse(root)
    root.mainloop()
