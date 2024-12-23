# Defining a simple class
class Dog:
    """A simple model of a dog."""

    def __init__(self, name, age):
        """Initialize the dog's name and age."""
        self.name = name  # Attribute
        self.age = age    # Attribute

    def sit(self):
        """Simulate the dog sitting."""
        print(f"{self.name} is now sitting.")

    def bark(self):
        """Simulate the dog barking."""
        print(f"{self.name} says Woof!")

# Creating an instance (object) of the Dog class
my_dog = Dog('Buddy', 3)

# Accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling methods
my_dog.sit()
my_dog.bark()