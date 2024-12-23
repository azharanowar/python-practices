def get_formated_name(first_name, last_name, middle_name=""):
    # Return neatly formated full name
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

print(get_formated_name("azhar", "anowar", "md"))

