# Defining a function that returns a dictionary
def build_function(first_name, last_name):
    # Return a dictionary of information of a person
    person = {
        "first": first_name,
        "last": last_name
    }

    return person

# Calling the function and storing returned dictionary to a variable
teacher = build_function("Abdur", "Rahman")

print(teacher)