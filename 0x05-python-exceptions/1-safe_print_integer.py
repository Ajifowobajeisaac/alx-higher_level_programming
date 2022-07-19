#!/usr/bin/python3

def safe_print_integer(value):
    '''a function that prints an integer with "{:d}".format()'''
    if value == int:
        try:
            print("{:d}".format(value))
            return True
        except ErrorIndex:
            pass
    else: 
        return False
