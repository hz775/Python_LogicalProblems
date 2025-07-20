import pytest
from calc import Calculator

@pytest.fixture
def calculator():
    return Calculator()

@pytest.mark.usefixtures("calculator")
class TestCalculator:

    @pytest.mark.basic
    def test_add(self, calculator):
        result = calculator.add(10, 5)
        assert result == 15

    @pytest.mark.basic
    def test_sub(self, calculator):
        result = calculator.sub(10, 5)
        assert result == 5

    @pytest.mark.advance
    def test_mul(self, calculator):
        result = calculator.mul(10, 5)
        assert result == 50

    @pytest.mark.advance
    def test_div(self, calculator):
        result = calculator.div(10, 5)
        assert result == 2

    @pytest.mark.error
    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError):
            calculator.div(10, 0)

    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 2),
        (9, 3, 3),
        (10, 5, 2),
    ])
    def test_divide(self, calculator, a, b, expected):
        result = calculator.div(a, b)
        assert result == expected
