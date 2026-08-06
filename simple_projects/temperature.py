# Create a function that converts the temperature from one measure to another

def farenheit(temp):
    """Converts celcius temperature to farenheit"""
    return (temp * (9/5)) + 32

def celcius(temp):
    """Converts the farenheit into celcius"""
    return (temp - 32) * (5 / 9)

def main():
    temperature = eval(input("Enter the temperature:"))
    convertion = input("To which measure it need to be converted:")
    if convertion.lower() == 'c':
        print(f"Temperature is converted into Celcius: {celcius(temperature)}℃ ")
    elif convertion.lower() == 'f':
        print(f"Temperature is converted into Farenheit: {farenheit(temperature)} ℉ ")
    else:
        print("Please enter to which measure the temperature needs to be converted!!")


if __name__ == "__main__":
    main()
