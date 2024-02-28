import math
from statistics import mean

class AdvancedCalculator:
    def add(self, x, y):
        return x + y

    def sine(self, angle):
        return math.sin(math.radians(angle))

    def mean(self, numbers):
        return mean(numbers)

    def exponentiation(self, x, y):
        return x ** y

    def square_root(self, x):
        return math.sqrt(x)
