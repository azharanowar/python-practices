"""A collection of mathematical functions..."""

def add(num1, num2):
    """Return the additional value of two perameters"""
    return num1 + num2

def sub(num1, num2):
    """Return the subtraction value of two perameters"""
    return num1 - num2

def mul(num1, num2):
    """Return the multiplication value of two perameters"""
    return num1 * num2

def div(num1, num2):
    """Return the divided value of two perameters or 'Infinity' if divide is not possible!"""
    if num2 == 0:
        return "Infinity"
    else:
        return num1 / num2