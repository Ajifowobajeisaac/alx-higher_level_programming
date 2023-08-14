#!/usr/bin/python3

"""A program that prints the number of and the list of its arguments."""

import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("0 arguments.")
    elif len(args) == 2:
        print(f"1 argument:")
        print(f"1: {args[1]}")
    else:
        print(f"{len(args) - 1} arguments:")
        arg_number = 1
        for arg in args[1:]:
            print(f"{arg_number}: {arg}")
            arg_number = arg_number + 1
