# Basic calculator
import sys
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

while True:
    print("Enter an operator for the calculation on the numbers:\n 1.Addition (+)\n 2.Substraction (-)\n 3.Multiplication (x)\n 4.Division (/)\n 5.Power (*)\n 6.quit to exit",end=' ')
    operator = input().lower()

    match operator:
        case '+':
            result = num1 + num2
            print(f"Addition of numbers {num1} + {num2} = {int(result) if result.is_integer() else result}.")
            break
        case '-':
            result = num1 - num2
            print(f"Substraction of numbers {num1} - {num2} = {int(result) if result.is_integer() else result}.")
            break
        case 'x':
            result = num1 * num2
            print(f"Multiplication of numbers {num1} x {num2} = {int(result) if result.is_integer() else result}.")
            break
        case '/':
            if num2 == 0:
                print("Division by zero is not possible")
                break
            result = num1 / num2
            print(f"Division of numbers {num1} / {num2} = {int(result) if result.is_integer() else result}.")
            break
        case '*':
            result = num1 ** num2
            print(f"Power of numbers {num1} power {num2} = {int(result) if result.is_integer() else result}.")
            break

        case "quit":
            sys.exit()

        case _:
            print("Enter a valid operator!!")
            

