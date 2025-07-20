import pytest 
from calc import Calculator

@pytest.fixture
def calc():
    print("\n[Fixture] Creating Calc object")
    return Calculator()

def test_add(calc):
    result=calc.add(10,5)
    assert result==15

def test_sub(calc):
    result=calc.sub(10,5)
    assert result==5

def test_mul(calc):
    result=calc.mul(10,5)
    assert result==50

