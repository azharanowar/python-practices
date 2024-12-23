# Example 9: Private Attribute

class Employee:
    """A class to represent an employee."""
    def __init__(self, name, position, salary):
        self.name = name                  # Public attribute
        self.position = position          # Public attribute
        self.__salary = salary            # Private attribute

    def display_info(self):
        """Display employee information."""
        print(f"Name: {self.name}, Position: {self.position}")

    def __display_salary(self):
        """Private method to display salary."""
        print(f"Salary: ${self.__salary}")

# Accessing public attributes
emp = Employee('John Doe', 'Manager', 75000)
print(emp.name)

# Accessing private attributes (Not recommended)
# print(emp.__salary)    # AttributeError: 'Employee' object has no attribute '__salary'

# Correct way to access private attribute (if necessary)
print(emp._Employee__salary)  # Name mangling allows access

# Accessing private method (Not recommended)
# emp.__display_salary()  # AttributeError

# Correct way to access private method
emp._Employee__display_salary()
