from src.math_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert sub(3,3)==0
    assert sub(5,3)==2