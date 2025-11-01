# Empty list
empty_list = []

# create variables of different types, assign values and assign some of them to the empty list as well as some literal values
# Do this with single instruction to popiulate the empty list with at least 8 different values
# Create variables of different types
int_var = 42
float_var = 3.14
string_var = "Hello"
boolean_var = True

# Populate the empty list
empty_list = [int_var, float_var, string_var, boolean_var, 100, 2.71, "World", False]

# Get two values from list by indexing
first_value = empty_list[0]  # 42
second_value = empty_list[1]  # 3.14

# Get two values from list by negative indexing
last_value = empty_list[-1]  # False

# Create dictionary with at least 4 key-value pairs
sample_dict = {
    "integer": int_var,
    "float": float_var,
    "string": string_var,
    "boolean": boolean_var
}

# Get a value from dictionary by key and update its value
sample_dict["float"] = 6.28  # Update float value

# Get keys(), values() and items() from dictionary
dict_keys = sample_dict.keys()
dict_values = sample_dict.values()
dict_items = sample_dict.items()

# Create tuple for a point in 2D space
point_2d = (10, 20)  # (x, y) coordinates

# Accessing tuple elements
x_coordinate = point_2d[0]
y_coordinate = point_2d[1]

# Create a tuple with a single element
single_element_tuple = (5,)  # Note the comma

# Create a set with at least 5 unique values
unique_set = {1, 2, 3, 4, 5}

# Create an empty set with set() function
empty_set = set()

# Create a set from a list
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(list_with_duplicates)  # {1, 2, 3, 4, 5}

# Use remove and discard methods on set
unique_set.remove(3)  # Removes 3 from the set
unique_set.discard(6)  # Does nothing as 6 is not in the set
unique_set.discard(4)  # Removes 4 from the set

