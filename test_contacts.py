from contacts_manager import validate_phone, validate_email

def test_phone():
    assert validate_phone("9876543210")[0] == True

def test_email():
    assert validate_email("test@example.com") == True

print("All tests passed!")