import pytest
import verify_password


def test_length():

    # check length
    # retrn true or false
    assert verify_password.check_length("Wjfjdhtttt") == True
    assert verify_password.check_length("Wjfj") == False

def test_has_number():

    assert verify_password.has_number("djflfj3lhhh") == True
    assert verify_password.has_number("djflfjlhhh") == False

def test_has_lower():

    assert verify_password.has_lower("dHjflfH23jlhhh") == True
    assert verify_password.has_lower("HHHHHHHHHH") == False

def test_has_upper():

    assert verify_password.has_upper("HHHHHHHHHH") == True
    assert verify_password.has_upper("hjsnuhn235") == False 

def test_make_upper():

    result = verify_password.make_upper("Hello World")
    assert result == "HELLO WORLD"
    assert type(result) is str
    assert "Wow" not in result

def test_check_password():
    
    assert verify_password.check_password("djHflf23jlhhh") == True 
    assert verify_password.check_password("djflf23jlhhh") == False  
