"""
Module to show example of error handling in Python.
"""

def divide_numbers(num1, num2):
    """
    Divides two numbers and handles division by zero error.

    Parameters:
    num1 (float): The numerator.
    num2 (float): The denominator.

    Returns:
    float: The result of the division if successful, None otherwise.
    """
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    else:
        return result
    
def read_file(file_path):
    """
    Reads a text file and returns its contents.

    Parameters:
    file_path (str): The path to the file to read.

    Returns:
    str: The contents of the file if successful, None otherwise.
    """
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def parse_json(json_string):
    """
    Parses a JSON string and returns the corresponding Python object.

    Parameters:
    json_string (str): The JSON string to parse.

    Returns:
    dict: The parsed JSON object if successful, None otherwise.
    """
    import json
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def access_list_element(lst, index):
    """
    Accesses an element from a list by index and handles index errors.

    Parameters:
    lst (list): The list to access.
    index (int): The index of the element to access.

    Returns:
    any: The element at the specified index if successful, None otherwise.
    """
    try:
        element = lst[index]
        return element
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")
        return None
    
    # Show example with finally block
def open_file_with_finally(file_path):
    """
    Opens a file and ensures it is closed after reading, using finally block.

    Parameters:
    file_path (str): The path to the file to open.

    Returns:
    str: The contents of the file if successful, None otherwise.
    """
    file = None
    try:
        file = open(file_path, 'r')
        contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if file is not None:
            file.close()