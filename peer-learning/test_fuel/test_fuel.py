from fuel import convert
from pytest import raises

# def test_guage():
#     assert guage('Twitter') == 'Twttr'
    

def test_convert():
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    
def test_convert_exceptions():
    with raises(ZeroDivisionError):
        convert('3/0')