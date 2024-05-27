import pytest
import math

@pytest.mark.square
def test_sqrt(num):
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def test_square():
    num = 8
    assert num*5 == 40

@pytest.mark.parametrize("a,b", [(10,11), (15,15)])
@pytest.mark.others
def test_equality(a,b):
    assert a == b
