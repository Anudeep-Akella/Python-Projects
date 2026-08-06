"""Fibonacci Sequence Calculates numbers of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13..."""

import sys

while True:
    while True:
        print("Enter the Nth Fibonacci number you wish to")
        print("calculate,(such as 5, 100, 1000 or 9999) or QUIT to quit.")
        response = input("> ").upper()

        if response == 'QUIT':
            print("Thank you for playing")
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break

        print("Enter a valid number or quit")
    print()

    if nth == 1:            # To print the first number if the given response is 1
        print('0')
        print()
        print('The #1 fibonacci number is 0.')
        continue
    elif nth == 2:          # To print the first 2 number if the given response is 2
        print('0,1')
        print()
        print('The #2 fibonacci number is 1.')
        continue

    if int(response) >= 10000:
        print('The given number is huge so it takes a while for printing')
        print('If you want to quit press ctrl+c')
        input('Enter to continue....')


    secondLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0,1, ',end='')

    while True:                     # Main loop to print fibonacci series
        nextNumber = secondLastNumber + lastNumber
        fibNumbersCalculated += 1

        print(nextNumber,end='')

        if fibNumbersCalculated == nth:
            print()
            print()
            print('The #',fibNumbersCalculated,' Fibonacci number is ',nextNumber,sep='')
            break

    print(',',end='')

    secondLastNumber = lastNumber
    lastNumber = nextNumber
