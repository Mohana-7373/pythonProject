import pytest

@pytest.mark.parametrize("a,b,c", [(1,2,3),(7,8,9)])
def test_functionAdd(a,b,c):
    assert a+b == c

@pytest.marks.parametrize("x,y,z",[(5,2,3),(6,2,3)])
def test_functionSub(a,b,c):
    assert a-b == c