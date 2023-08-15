#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all the integers of a list in reverse order."""
    my_list = sorted(my_list, reverse=True)
    for item in my_list:
        print("{}".format(item))
