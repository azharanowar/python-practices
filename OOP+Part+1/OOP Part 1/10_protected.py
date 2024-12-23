# Example 10: Protected Attribute

class Employee:
    """A class to represent an employee."""
    def __init__(self, name, position, salary):
        self.name = name                  # Public attribute
        self.position = position          # Public attribute
        self._salary = salary             # Protected attribute

    def display_info(self):
        """Display employee information."""
        print(f"Name: {self.name}, Position: {self.position}")

# Accessing protected attribute
emp = Employee('John Doe', 'Manager', 75000)
print(emp._salary)

# While it's accessible, it's an indication that it should not be modified directly
emp._salary = 80000           # Not recommended

print(emp._salary)
