#!/usr/bin/python3
def no_c(my_string):
    str = ''
    new_string = my_string.translate({ord(i): str for i in 'cC'})
    return new_string
