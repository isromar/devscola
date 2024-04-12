# test_thegreeting.py

from thegreeting.thegreeting import greet

def test_thegreeting():
    nameOfPerson = 'Mary'
    result = greet(nameOfPerson)
    assert result == 'Hello, Mary'
    
    nameOfPersonNull = ""
    result = greet(nameOfPersonNull)
    assert result == 'Hello, my friend'