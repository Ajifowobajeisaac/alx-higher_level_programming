#!/usr/bin/python3
def uppercase(str):
    ascii_values = [chr(ord(c)-32) for c in str]
    print("{}".format(ascii_values), end="")
