print(f"Without importing a module the name is {__name__}")

import module.my_module as my_module

my_module.test_function()