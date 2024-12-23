# Example 4: Accessing Attributes and Modifying Attributes 

class Student:
    """A class to represent a student."""
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

# Creating an instance
student = Student('Ali', 20, 'Computer Engineering')

# Accessing attributes
print(f"Name: {student.name}")
print(f"Age: {student.age}")
print(f"Major: {student.major}")


# Modifying Object Attributes

# Modifying attribute values
student.age = 21
student.major = 'Data Science'

print(f"Updated Age: {student.age}")
print(f"Updated Major: {student.major}")
