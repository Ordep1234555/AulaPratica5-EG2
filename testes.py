from calculator import MemoryCalculator

def test_sum_is_zero_on_initialization():
    calculator = MemoryCalculator()
    assert calculator.sum() == 0

def test_sum_one_number():
    calculator = MemoryCalculator()
    calculator.add(5)
    assert calculator.sum() == 5

def test_sum_two_numbers():
    calculator = MemoryCalculator()
    calculator.add(5)
    calculator.add(10)
    assert calculator.sum() == 15

def test_sum_is_zero_after_calling_sum():
    calculator = MemoryCalculator()
    calculator.add(5)
    calculator.sum()  # resultado: 5
    assert calculator.sum() == 0

def test_sum_numbers_and_save_last_sum():
    calculator = MemoryCalculator()
    calculator._save_last_sum = True
    calculator.add(5)
    calculator.add(10)
    calculator.sum()
    calculator.add(15)
    assert calculator.last_sum + calculator.sum() == 30
