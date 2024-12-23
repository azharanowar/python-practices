# defining a function that returns a value
def get_formatted_name(first_name, middle_name, last_name):
    """return a full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
#calling the function and storing the return value jn a variable
student = get_formatted_name("amir", " sharif", "ahmed")
print(student)