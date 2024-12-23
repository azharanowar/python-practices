# Example 3: Creating Objects

class Dog:
    """A simple model of a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances of the Dog class
my_dog = Dog('Buddy', 3)
your_dog = Dog('Max', 5)

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name}.")
print(f"Your dog's name is {your_dog.name}.")
