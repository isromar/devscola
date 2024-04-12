# test_fizzbuzz.py

from fizzbuzz.fizzbuzz import checkDivisors

def test_fizzbuzz():
    divisibleByThree = 3
    resultado = checkDivisors(divisibleByThree)
    assert resultado == 'Fizz'
    
    divisibleByFive = 5
    resultado = checkDivisors(divisibleByFive)
    assert resultado == 'Buzz'
    
    divisibleByThreeAndFive = 30
    resultado = checkDivisors(divisibleByThreeAndFive)
    assert resultado == 'FizzBuzz'
    
    notDivisibleByNeitherThreeNorFiveNorHasAThreeNorFive = 88
    resultado = checkDivisors(notDivisibleByNeitherThreeNorFiveNorHasAThreeNorFive)
    assert resultado == '88'
