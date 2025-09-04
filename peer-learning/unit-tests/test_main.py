from main import add, divide

import pytest
#from pytest import raises

def test_add():
    assert add(1,3) == 4, 'Expects 1 + 3 to equal 4'

def test_division():
    with pytest.raises(ZeroDivisionError):
        divide(1,0)