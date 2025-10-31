import tkinter as tk
from tkinter import ttk
from pathlib import Path
import os

class FileSystemTree:
    def __init__(self, root):
        self.root = root
        self.root.title("File System Explorer")
        self.root.geometry("800x600")
        
        # Create main container
        self.main_frame = ttk.Frame(root, padding="5")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for resizing
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        
        # Create path entry field
        self.path_label = ttk.Label(self.main_frame, text="Path:")
        self.path_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        
        self.path_var = tk.StringVar()
        self.path_entry = ttk.Entry(self.main_frame, textvariable=self.path_var, width=50)
        self.path_entry.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Create Browse button
        self.browse_button = ttk.Button(self.main_frame, text="Browse", command=self.browse_path)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Create Treeview
        self.tree = ttk.Treeview(self.main_frame, selectmode='browse')
        self.tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Define folder and file symbols
        self.folder_image = "▶"  # Triangle for folders
        self.file_image = "•"    # Bullet for files
        
        # Create custom style for treeview with larger font for icons
        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Segoe UI", 10))
        self.tree.configure(style="Treeview")
        
        # Configure tags for folder and file colors
        self.tree.tag_configure('folder', foreground='#FFB900')  # Yellow-gold color for folders
        self.tree.tag_configure('file', foreground='#666666')    # Gray for files
        
        # Add scrollbar
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=1, column=3, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Bind events - update on Enter or focus loss
        self.path_entry.bind('<Return>', self.update_tree)
        self.path_entry.bind('<FocusOut>', self.update_tree)
        
        # Initialize with current directory
        self.path_var.set(os.getcwd())
        self.update_tree()
        
    def browse_path(self):
        """Open file dialog to browse for path"""
        from tkinter import filedialog
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)
            self.update_tree()
    
    def validate_path(self, path):
        """Check if path exists and is valid"""
        return os.path.exists(path)
    
    def update_tree(self, event=None):
        """Update the treeview with the current path"""
        path = self.path_var.get()
        if not self.validate_path(path):
            return
            
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Add root folder name (not full path)
        folder_name = Path(path).name or path  # Use path if name is empty (like for root drive)
        root_node = self.tree.insert('', 'end', 
                                   text=f"{self.folder_image} {folder_name}", 
                                   open=True,
                                   tags=('folder',))
        self.populate_tree(root_node, path)
    
    def populate_tree(self, parent, path):
        """Recursively populate the tree"""
        try:
            # Sort directories first, then files
            paths = sorted(Path(path).iterdir(), 
                         key=lambda x: (not x.is_dir(), x.name.lower()))
            
            for item in paths:
                try:
                    # Create node name with icon
                    is_directory = item.is_dir()
                    icon = self.folder_image if is_directory else self.file_image
                    node_text = f"{icon} {item.name}" + ('/' if is_directory else '')
                    
                    # Insert node with appropriate tag
                    node = self.tree.insert(
                        parent, 'end', 
                        text=node_text,
                        tags=('folder' if is_directory else 'file')
                    )
                    
                    # Recursively populate if it's a directory
                    if is_directory:
                        self.populate_tree(node, item)
                except PermissionError:
                    # Handle permission errors gracefully
                    self.tree.insert(parent, 'end', 
                                   text=f"{self.file_image} {item.name} (Access Denied)",
                                   tags=('file',))
        except PermissionError:
            self.tree.insert(parent, 'end', 
                           text=f"{self.folder_image} Access Denied",
                           tags=('folder',))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemTree(root)
    root.mainloop()
