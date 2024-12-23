# Example 8: Public Attribute

class Employee:
    """A class to represent an employee."""
    def __init__(self, name, position):
        self.name = name          # Public attribute
        self.position = position  # Public attribute

    def display_info(self):
        """Display employee information."""
        print(f"Name: {self.name}, Position: {self.position}")

# Accessing public attributes
emp = Employee('John Doe', 'Manager')
print(emp.name)
emp.display_info()