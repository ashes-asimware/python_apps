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