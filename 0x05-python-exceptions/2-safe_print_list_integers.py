#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ''' a function that prints the first x elements of a list and only integers.'''
    count = 0

    for i in range(x):
        while x == int:
            try:
                print("{:d}".format(i))
            except: (TypeError, ValueError):
                break
    print("")
    return counter
