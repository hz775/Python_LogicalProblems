import pytest
from calc import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.basic
def test_add(calculator):
    result=calculator.add(10,5)
    assert result==15

@pytest.mark.basic
def test_sub(calculator):
    result=calculator.sub(10,5)
    assert result==5

@pytest.mark.advance
def test_mul(calculator):
    result=calculator.mul(10,5)
    assert result==50

@pytest.mark.advance
def test_div(calculator):
    result=calculator.div(10,5)
    assert result==2

@pytest.mark.error
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.div(10,0)

@pytest.mark.parametrize("a, b, expected", [
    (4, 2, 2),
    (9, 3, 3),
    (10, 5, 2),
])
def test_divide(calculator, a, b, expected):
    result=calculator.div(a,b)
    assert result == expected

@pytest.mark.xfail
def test_add_fail(calculator):
    result=calculator.add(2,2)
    assert result==5

@pytest.mark.xfail(strict=True)
def test_add_fail_expected():
    result=calculator.add(2,2)
    assert result==4 # This will unexpectedly pass, so pytest will fail it

@pytest.mark.skip(reason="Not implemented yet")
def test_login_feature():
    assert False  # Will be skipped

