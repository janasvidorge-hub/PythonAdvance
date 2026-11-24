import re

def validate_password(password):
    # At least 8 characters, with one uppercase letter, one digit,
    # and one special character.
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"
    return re.match(pattern, password) is not None


password = input("Enter a password: ")

if validate_password(password):
    print("Password is valid.")
else:
    print(
        "Password is invalid. It must be at least 8 characters long "
        "and include an uppercase letter, a digit, and a special character."
    )