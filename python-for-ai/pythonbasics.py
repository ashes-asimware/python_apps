# Show print statement
print("This is a Python basics file.")

# Show variable assignment
x = 10
y = 20

"""
Show multi line comment stating addition of two variables
x and y and printing the result.
"""
print("The sum of x and y is:", x + y)

# Show exponentiation
result = x ** 2

# Show string concatenation with first_name and last_name variables, omit print statement
first_name = "John" 
last_name = "Doe"
full_name = first_name + " " + last_name

# Show boolean variable assignment
is_active = True

# Show assignment of boolean expression to a variable
is_greater = x > y

# Show logical AND operation
is_valid = is_active and is_greater

# Show logical OR operation
is_either = is_active or is_greater

# Draw a 2x2 truth table for both AND and OR operations using comments
# | is_active | is_greater | is_valid |
# |-----------|------------|----------|
# |    T      |     T      |    T     |
# |    T      |     F      |    F     |
# |    F      |     T      |    F     |
# |    F      |     F      |    F     |

# OR Truth Table
# | is_active | is_greater | is_either |
# |-----------|------------|-----------|
# |    T      |     T      |     T     |
# |    T      |     F      |     T     |
# |    F      |     T      |     T     |
# |    F      |     F      |     F     |

# Print statement using f-string to display full_name
print(f"Full name is: {full_name}")

# Show if elif else statement to check if x is greater than, less than, or equal to y
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# Show for loop with range
for i in range(0,10,2):
    print("Iteration:", i)