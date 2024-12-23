# Example 6: Using self in Methods

class Rectangle:
    """A class to represent a rectangle."""
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def sub(self):
        """Calculate substruct value from height to width"""
        return self.height - self.width

# Creating an instance
rect = Rectangle(5, 3)

# Calling methods
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Subtruction value: {rect.sub()}")
