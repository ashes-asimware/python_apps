def greet():
    print("Hello!")

greet()  # Call the function to display the greeting

# Create greet function that takes a name as parameter and prints greeting message
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")  # Call the function with a name parameter

# Create a greet_full_name function that takes first and last name as parameters and prints greeting message
def greet_full_name(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet_full_name("Alice", "Smith")  # Call with named parameters and pass parameters in arbitrary order
greet_full_name(last_name="Smith", first_name="Alice")  # Call with named parameters

# Show variable scope
x = 10
y = 5

def add():
    return x + y

add()

# Create a function that takes x and y and returns their sum
def add_xy(x, y):
    return x + y

# Call add_xy with named parameters in arbitrary order
result = add_xy(y=5, x=10)

# Function to calculate area of room using length and width parameters
def calculate_area(length, width):
    return length * width

area = calculate_area(length=10, width=5)  # Call with named parameters

# Use the calculate_area function in a conditional statement
if area > 50:
    print("Large room")
else:
    print("Small room")

# Create function to return first and last element of an unordered list
def first_and_last(input_list):
    if len(input_list) == 0:
        return None, None
    return input_list[0], input_list[-1]

first, last = first_and_last([5, 2, 3, 4, 1])
