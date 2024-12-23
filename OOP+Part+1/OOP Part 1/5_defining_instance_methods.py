# Example 5: Defining Instance Methods

class Student:
    """A class to represent a student."""
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        """Instance method to introduce the student."""
        print(f"Hello, my name is {self.name}. I'm {self.age} years old, studying {self.major}.")

# Creating an instance
student = Student('Ali', 20, 'AI')

# Calling an instance method
student.introduce()
