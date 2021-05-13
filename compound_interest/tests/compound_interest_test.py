import unittest

from src.compound_interest import CompoundInterest


class CompoundInterestTest(unittest.TestCase):

    # Tests
    def setUp(self):
        self.interest_calculator = CompoundInterest(12)

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_100_at_10_for_20(self):
        self.assertEquals(732.81, self.interest_calculator.calculate(100, 0.10, 20))

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_100_at_6_for_10(self):
        self.assertEquals(181.94, self.interest_calculator.calculate(100, 0.06, 10))

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_100000_at_5_for_8(self):
        self.assertEqual(149058.55, self.interest_calculator.calculate(100000, 0.05, 8))

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_0_at_10_for_1(self):
        self.assertEqual(0.0, self.interest_calculator.calculate(0, 0.10, 1))

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_100_at_0_for_10(self):
        self.assertEqual(100.0, self.interest_calculator.calculate(100, 0, 10))


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test_100_at_5_for_8_contributing_1000(self):
        self.assertEqual(118380.16, self.interest_calculator.calculate_with_cont(100, 0.05, 8, 1000))
    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

