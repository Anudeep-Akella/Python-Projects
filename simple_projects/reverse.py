# Create a function that returns the reverse of the given string

def reverse(string):
    """Reverses the given string"""
    if string == "":
        return "The input must not be empty!"
    return string[::-1]

def main():
    my_str = input("Enter a string:")
    print("Reversed string:",reverse(my_str))

if __name__ == "__main__":
    main()
