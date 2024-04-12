# test_suma.py

from sum.another_sum import suma

def test_suma():
    num1 = 5
    num2 = 10
    
    resultado = suma(num1, num2)
    
    assert resultado == 15
