# test_fizzbuz.py
from fizzbuzz.fizzbuzz import FizzBuzz

def test_get_list_should_be_a_list_from_number_one_to_one_hundred():
    # Arrange
    fizz_buzz = FizzBuzz()

    # Act
    result = fizz_buzz.get_list()

    # Assert
    assert len(result) == 100

def test_get_list_first_position_should_be_one():
    fizz_buzz = FizzBuzz()
    
    result = fizz_buzz.get_list()
    
    assert result[0] == 1

def test_get_list_last_position_should_be_one_hundred():
    fizz_buzz = FizzBuzz()
    
    result = fizz_buzz.get_list()
    
    assert result[99] == 100
    
def test_get_list_middle_position_should_be_between_one_and_one_hundred():
    fizz_buzz = FizzBuzz()
    
    result = fizz_buzz.get_list()
    
    assert result[55] == 56
        
def test_check_divisors_when_divisible_by_three_should_be_Fizz():
    fizz_buzz = FizzBuzz()
    
    divisible_by_three = 3
    result = fizz_buzz.check_divisors(divisible_by_three)
    assert result == 'Fizz'
    
    divisible_by_three = 33
    result = fizz_buzz.check_divisors(divisible_by_three)
    assert result == 'Fizz'

def test_check_divisors_when_divisible_by_five_should_be_buzz():
    fizz_buzz = FizzBuzz()
    
    divisible_by_five = 5
    result = fizz_buzz.check_divisors(divisible_by_five)
    assert result == 'Buzz'

def test_check_divisors_when_divisible_by_five_and_three_should_be_Fizzbuzz():
    fizz_buzz = FizzBuzz()
    
    divisible_by_three_and_five = 30
    result = fizz_buzz.check_divisors(divisible_by_three_and_five)
    assert result == 'FizzBuzz'

def test_check_divisors_when_not_divisible_by_neither_three_nor_five_should_be_the_number_as_string():
    fizz_buzz = FizzBuzz()
    
    not_divisible_by_neither_three_nor_five = 88
    result = fizz_buzz.check_divisors(not_divisible_by_neither_three_nor_five)
    
    assert result == '88'

def test_check_divisors_when_is_divisible_by_three_or_if_it_has_a_three_in_it_should_be_Fizz():
    fizz_buzz = FizzBuzz()
    
    divisible_by_three_or_has_a_three_in_it = 13
    result = fizz_buzz.check_divisors(divisible_by_three_or_has_a_three_in_it)
    
    assert result == 'Fizz'

def test_check_divisors_when_is_divisible_by_five_of_if_it_has_a_five_in_it_should_be_Buzz():
    fizz_buzz = FizzBuzz()
    
    divisible_by_five = 20
    result = fizz_buzz.check_divisors(divisible_by_five)
    assert result == 'Buzz'
        
    has_a_five_in_it = 52
    result = fizz_buzz.check_divisors(has_a_five_in_it)
    assert result == 'Buzz'
    
