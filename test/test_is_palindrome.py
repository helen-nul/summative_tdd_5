from main import is_palindrome

def test_pytest():
    assert 3+3 == 6 

def test_is_palindrome_happy():
    assert is_palindrome("radar") == True