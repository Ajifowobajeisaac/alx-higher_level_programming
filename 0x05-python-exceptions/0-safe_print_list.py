#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''Print a list of x elements'''

    counter = 0
    for i in range(x):
        try:
            print(my_list[i]), end="")
            counter += 1
        except IndexError:
            break
    print("")
    return (counter)
