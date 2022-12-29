import pytest


@pytest.mark.parametrize("x,y,z",[(5,2,3),(6,2,3)])
def test_functionSub(x,y,z):
    assert x-y == z

