# Create a function for email validation

import re
def validation(email):
    """Function for validation of email address using regex expressions"""
    if email == "":
        return "Enter a email!"
    pattern = r'^[a-zA-Z0-9._%-+]+@[a-zA-z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern,email))

email = input("Enter an email for validation check:")
result = validation(email)
if result:
    print("Valid email Address!")
else:
    print("Not a valid email Address!")

