# Create a function for email validation
# A email is valid only if the email follows the structured format email's must have including the '@' symbol and domain name.

import re  # Import built in module for the Regular Expressions

def validation(email):
    """Function for validation of email address using regex expressions"""

    if email == "":
        return "Enter a email!"

    if isinstance(email,(int,float)) or not isinstance(email,str):
        return "Enter a Valid String!!"

    pattern = r'^[a-zA-Z0-9._%-+]+@[a-zA-z0-9.-]+\.[a-zA-Z]{2,}$'
    if bool(re.fullmatch(pattern,email)):
        return "Valid Email Address!"
    return "Not a Valid Email Address!!"


email = input("Enter an email for validation check:")
print(validation(email))

