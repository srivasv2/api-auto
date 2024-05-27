import pytest
@pytest.mark.compare
def test_greater():
    num = 100
    assert num > 100
@pytest.mark.compare
def test_greater_equal():
    num = 100
    assert num >= 100
@pytest.mark.compare
def test_less():
    num = 100
    assert num < 200