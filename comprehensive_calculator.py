import math
from statistics import mean, median

class ComprehensiveCalculator:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero.")

    def logarithm(self, x):
        return math.log10(x)

    def tangent(self, angle):
        return math.tan(math.radians(angle))

    def median(self, numbers):
        return median(numbers)

    def exponentiation(self, x, y):
        return x ** y

    def square_root(self, x):
        return math.sqrt(x)
