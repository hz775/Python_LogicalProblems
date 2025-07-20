from calc import add,div,sub,mul
import pytest

def test_addition():
    assert add(10,5)==15
    assert add(1,2)==3

def test_subraction():
    assert sub(10,5)==5
    assert sub(2,1)==1

def test_division():
    assert div(10,5)==2
    assert div(2,1)==2

def test_multiplication():
    assert mul(10,5)==50
    assert mul(2,1)==2

def test_division_with_zero():
    with pytest.raises(ValueError,match="divide by zero"):
        div(10,0)


@pytest.fixture
def sample_list():
    return [1, 2, 3]

def test_sum(sample_list):
    assert sum(sample_list) == 6




