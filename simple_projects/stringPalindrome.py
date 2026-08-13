# String Palindrome function
# Palindrome means the value must be equal to its reverse order.
# Ex madam reverse order is also madam so it's a palindrome string.
# sir reverse order is not sir so it's not a palindrome string.

def palindrome(string):
    """Checks for the Palindrome of a string"""
    if string == "":
        return "Please enter a string!!"
    if isinstance(string,(int,float)) or not isinstance(string,str):
        return "Please enter a valid string!!"
    if string == string[::-1]:
        return "A Palindrome"
    return "Not A Palindrome"

string = input("Enter the string to check the string is palindrome or not:")
print(f"Given string {string} is {palindrome(string)}.")
