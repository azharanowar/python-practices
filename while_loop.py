def get_full_name(first_name, last_name, middle_name=""):
    # Return neatly formated full name
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


print(get_full_name("Azhar", "Anowar"))
print(get_full_name("Azhar", "Anowar", "Md"))

def build_function(first_name, last_name):
    # Return a dictionary of information of a person
    person = {
        "first": first_name,
        "last": last_name
    }

    return person

teacher = build_function("Abdur", "Rahman")
print(teacher)


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"

    return full_name.title()


while True:
    print("Enter 'q' for quit...")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    if(first_name == 'q'):
        break
    elif(last_name == 'q'):
        break
    else:
        print(f"{first_name} {last_name}")


