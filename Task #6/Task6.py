# Q No 01
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

# Class representing a Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
r = float(input("Enter radius of circle: "))
c = Circle(r)

print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())

# Q No 03
# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
# Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."


# Example usage
calc = Calculator()

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition:", calc.add(x, y))
print("Subtraction:", calc.subtract(x, y))
print("Multiplication:", calc.multiply(x, y))
print("Division:", calc.divide(x, y))
