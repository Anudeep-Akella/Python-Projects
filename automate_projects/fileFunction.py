# A program to add create and add the content to the file user specified

def writeToFile(name,content):
    """Function to create and write content to the specified file"""

    with open(name,'w') as file:
    
        file.write(content)

def readFile(name):
    """Function to read the contents of the specified file"""
  
    with open(name,'r') as file:
        return file.read()

def main():
    name = input('Enter the file name or file path: ')
    if name == '':
        return "Please enter a valid file name or file path"
    
    content = input('Enter the content you want to enter into the file: ')

    if content == '':
        return "The content into the file must be non empty"

    writeToFile(name,content)
    result = readFile(name)
    return result


if __name__ == "__main__":
    output = main()
    print(output)
    
    
