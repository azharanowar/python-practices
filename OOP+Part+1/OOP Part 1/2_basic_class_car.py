# Example 2: Defining a Basic Class

class Car:
    """A simple class to represent a car."""

    def __init__(self, make, model, year):
        """Initialize the car's attributes."""
        self.make = make      # Instance attribute
        self.model = model    # Instance attribute
        self.year = year      # Instance attribute

# Creating an instance of the Car class
my_car = Car('Hyundai', 'Sonata', 2020)

# Accessing instance attributes
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")
