# import module.my_module

# my_module = module.my_module
# my_module.test_function()
# my_module.greet_user("Anowar")




# Importing a method/function only from a module without importing entire module:
# from module.my_module import greet_user
from module.my_module import greet_user, test_function # For mutiple use comma...

greet_user("Anowar")


# Importing module as anther name
import module.my_module as my_first_module
my_first_module.greet_user("Anowar")


# Importing a function from a module with another name
from module.my_module import greet_user as greet
greet("R.afi")

