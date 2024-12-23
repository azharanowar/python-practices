# def greeting_students(names):
#     names.append("taohid") # Modyfying a list from a function as a parameter will affect the main list because the function use address/refernce of the list not a new list created
#     for name in names:
#         print(f"Hello {name.title()}! How are you today?")


# names_of_students = ["anowar", "rafi", "sijan"]

# greeting_students(names_of_students)
# print(names_of_students)


# def removing_elements(input_list, elements_to_remove):
#     for item in input_list:
#         if item in elements_to_remove:
#             input_list.remove(item) # Safe remove of element by checking if element exist
#         print(item)

# initial_list = [1, 2, 4, 5, 6]
# elements_to_remove = [2, 3, 4]

# removing_elements(initial_list, elements_to_remove)
# print(initial_list)


def removing_elements(input_list, elements_to_remove):
    for item in input_list:
        if item in elements_to_remove:
            input_list.remove(item) # Safe remove of element by checking if element exist
        print(item)

initial_list = [1, 2, 4, 5, 6]
elements_to_remove = [2, 3, 4]

# Passing copy of list as an argument in a function so that original list will not be modified or affected...
removing_elements(initial_list[:], elements_to_remove)
# removing_elements(initial_list.copy(), elements_to_remove) # Alternative way with copy() method
print(initial_list)