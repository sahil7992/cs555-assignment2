import unittest
from advanced_calculator import AdvancedCalculator

class TestAdvancedCalculator(unittest.TestCase):

    def test_addition(self):
        calc = AdvancedCalculator()
        result = calc.add(5, 7)
        expected_result = 12
        self.assertEqual(result, expected_result)
        print(f"Test Addition: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_trigonometric_function(self):
        calc = AdvancedCalculator()
        result = round(calc.sine(30),2)
        expected_result = 0.5
        self.assertAlmostEqual(result, expected_result, places=2)
        print(f"Test Trigonometric Function: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_statistical_calculation(self):
        calc = AdvancedCalculator()
        result = calc.mean([2, 4, 6, 8, 10])
        expected_result = 6
        self.assertEqual(result, expected_result)
        print(f"Test Statistical Calculation: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_exponentiation(self):
        calc = AdvancedCalculator()
        result = calc.exponentiation(2, 3)
        expected_result = 8
        self.assertEqual(result, expected_result)
        print(f"Test Exponentiation: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

    def test_square_root(self):
        calc = AdvancedCalculator()
        result = calc.square_root(25)
        expected_result = 5
        self.assertEqual(result, expected_result)
        print(f"Test Square Root: {result} == {expected_result}")
        print("Pass\n" if result == expected_result else "Fail\n")

if __name__ == '__main__':
    unittest.main()
