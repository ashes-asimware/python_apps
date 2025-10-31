import os
from pathlib import Path

def traverse_directory(path, level=0):
    """
    Recursively traverse a directory and print all files and folders with indentation.
    
    Args:
        path: String or Path object representing the directory to traverse
        level: Current indentation level (internal use for recursion)
    """
    try:
        # Convert string path to Path object if needed
        directory = Path(path)
        
        # Check if the path exists and is a directory
        if not directory.exists():
            print(f"Error: Path '{directory}' does not exist.")
            return
        if not directory.is_dir():
            print(f"Error: Path '{directory}' is not a directory.")
            return
            
        # Traverse the directory
        for item in directory.iterdir():
            # Create indentation based on level
            indent = "    " * level
            # Print item name with type indicator and indentation
            if item.name != ".git":
                print(f"{indent}{'[DIR]' if item.is_dir() else '[FILE]'} {item.name}")
            # If it's a directory, recursively traverse it
                if item.is_dir():
                    traverse_directory(item, level + 1)
              
    except PermissionError as e:
        print(f"Permission denied accessing {path}: {e}")
    except Exception as e:
        print(f"Error traversing {path}: {e}")

if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        # Use directory path provided as command line argument
        directory_path = sys.argv[1]
    else:
        # Use current directory if no path provided
        directory_path = "."
    
    print(f"Traversing directory: {directory_path}")
    traverse_directory(directory_path)
