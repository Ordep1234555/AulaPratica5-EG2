import unittest
from calculator import MemoryCalculator

class TestMemoryCalculator(unittest.TestCase):

  def test_sum_is_zero_on_initialization(self):
    calculator = MemoryCalculator()
    self.assertEqual(0, calculator.sum())

  def test_sum_one_number(self):
    calculator = MemoryCalculator()
    calculator.add(5)
    self.assertEqual(5, calculator.sum())

  def test_sum_two_numbers(self):
    calculator = MemoryCalculator()
    calculator.add(5)
    calculator.add(10)
    self.assertEqual(15, calculator.sum())

  def test_sum_is_zero_after_calling_sum(self):
    calculator = MemoryCalculator()
    calculator.add(5)
    calculator.sum() # resultado: 5
    self.assertEqual(0, calculator.sum())

  def test_sum_numbers_and_save_last_sum(self):
    calculator = MemoryCalculator()
    calculator._save_last_sum = True
    calculator.add(5)
    calculator.add(10)
    calculator.sum()
    calculator.add(15)
    self.assertEqual(30, calculator.last_sum + calculator.sum())
