import os

from art import logo
from helpers import operations


def calculator():
    try:
        print(logo)
        num1 = float(input("What's the first number?: "))
    
        for symbol in operations:
            print(symbol)

        should_continue = True

        while should_continue:        
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
                num1 = answer
            else:
                os.system("clear")
                should_continue = False
                calculator()


    except ValueError as ve:
        print("ERROR:Please enter a integer number!")


if __name__ == "__main__":
    calculator()
