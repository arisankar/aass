import pytest

def test_func1():
    print("hello")
@pytest.mark.smoke
def test_func2():
    print("hi")