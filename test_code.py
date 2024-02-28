import unittest
from comprehensive_calculator import ComprehensiveCalculator

class TestComprehensiveCalculator(unittest.TestCase):

    def test_addition(self):
        calc = ComprehensiveCalculator()
        result = calc.add(5, 7)
        expected_result = 12
        self.assertEqual(result, expected_result)
        print(f"Test Addition: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_multiplication(self):
        calc = ComprehensiveCalculator()
        result = calc.multiply(10, 3)
        expected_result = 30
        self.assertEqual(result, expected_result)
        print(f"Test Multiplication: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_division(self):
        calc = ComprehensiveCalculator()
        result = calc.divide(15, 3)
        expected_result = 5
        self.assertEqual(result, expected_result)
        print(f"Test Division: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_logarithmic_function(self):
        calc = ComprehensiveCalculator()
        result = calc.logarithm(100)
        expected_result = 2
        self.assertEqual(result, expected_result)
        print(f"Test Logarithmic Function: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_advanced_trigonometric_function(self):
        calc = ComprehensiveCalculator()
        result = calc.tangent(45)
        expected_result = 1
        rounded_result = round(result)  
        self.assertEqual(rounded_result, expected_result)
        print(f"Test Advanced Trigonometric Function: {rounded_result} == {expected_result}")
        print("Pass\n" if rounded_result == expected_result else "Fail\n")

    def test_statistical_calculation(self):
        calc = ComprehensiveCalculator()
        result = calc.median([2, 4, 6, 8, 10])
        expected_result = 6
        self.assertEqual(result, expected_result)
        print(f"Test Statistical Calculation: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_exponentiation(self):
        calc = ComprehensiveCalculator()
        result = calc.exponentiation(2, 4)
        expected_result = 16
        self.assertEqual(result, expected_result)
        print(f"Test Exponentiation: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_square_root(self):
        calc = ComprehensiveCalculator()
        result = calc.square_root(36)
        expected_result = 6
        self.assertEqual(result, expected_result)
        print(f"Test Square Root: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

if __name__ == '__main__':
    unittest.main()
