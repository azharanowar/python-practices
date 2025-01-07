# def make_shirt(size, message):
#     print(f"The size of the shirt is: {size}")
#     print(f"The message is: {message}")


# make_shirt("XL", "Exam ka hal keya hey?") # Function calling with positional arguments
# make_shirt(message="Keya hal hei?", size="L") # Function calling with keyword arguments


# def describe_city(city_name, country_name="Bangladesh"):
#     print(f"Your city name is {city_name} and country name is {country_name}")
# while True:
#     user_city = input("Enter your city name: ")
#     user_country = input("Enter your country name: ")

#     if user_city == "quit" or user_country == "quit":
#         break
#     else:
#         describe_city(user_city, user_country)



def dic_return_function():
    return {
        1:"Hello",
        'name': "Anowar",
        'age': 24
    }

returned_value = dic_return_function()
print(returned_value)


def get_full_name(first_name, last_name, middle_name=""):
    return f"{first_name} {middle_name} {last_name}"




while True:
    print("Enter 'q' to exit the program: ")
    user_first_name = input("Enter yuur first name: ")
    user_middle_name = input("Enter your middle name: ")
    user_last_name = input("Enter your last name: ")

    if user_first_name == "q" or user_middle_name == "q" or user_last_name == "q":
        break 
    
    print(get_full_name(user_first_name.strip(), user_last_name.strip(), user_middle_name.strip()))




# List: append(), insert(), extend(), remove(), pop(), clear()