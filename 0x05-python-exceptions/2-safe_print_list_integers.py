#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    '''a function that prints the integers in a list.'''
    count = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print("")
    return count
