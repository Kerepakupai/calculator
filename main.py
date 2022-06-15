from cmath import log
import os
from art import logo

def add(n1, n2):
    """ Take two numbers and return the add """
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    os.system('clear')
    print(logo)

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    num1 = float(input("What's the first number?: "))
    should_continue = True
    for symbol in operations:
            print(symbol)

    while should_continue: 
        operaction_symbol = input('Pick an operation: ')
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operaction_symbol]
        answer = calculation_function(num1, num2)
        
        print(f'{num1} {operaction_symbol} {num2} = {answer}')
        
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

if __name__ == '__main__':
    calculator()