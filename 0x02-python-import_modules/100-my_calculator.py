#!/usr/bin/python3

"""
    A basic calculator with 4 operations.

    Usage: ./100-my_calculator.py <a> <operator> <b>
    Arguments:
        <a> int: Left hand integer.
        <operator>: The mathematical operation.
        <b> int: Right hand integer.
"""

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(args[1])
        operator = args[2]
        b = int(args[3])

        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            result = div(a, b)

        operators = ['+', '-', '*', '/']
        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            print(f"{a} {operator} {b} = {result}")
