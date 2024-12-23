# Example 7: Implementing __str__ and __repr__ Methods

class Student:
    """A class to represent a student."""
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        """Return a readable string representation of the student."""
        return f"{self.name}, Age: {self.age}, Major: {self.major}"

    def __repr__(self):
        """Return a detailed string representation of the student."""
        return f"Student('{self.name}', {self.age}, '{self.major}')"

# Creating an instance
student = Student('Ali', 20, 'Computer Science')

# Using __str__
print(str(student))  # or simply print(student)

# Using __repr__
print(repr(student))
