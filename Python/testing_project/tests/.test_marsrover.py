# test_marsrover.py

from marsrover.marsrover import checkLandingPosition

def test_marsrover():
    landingPosition = "5,5,N"
    command = ""
    result = checkLandingPosition(landingPosition, command)
    assert result == "5,5,N"
    