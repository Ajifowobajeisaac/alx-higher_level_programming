#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string"""

    upd_string = ''
    for new_string in my_string:
        if 'B' not in new_string:
            upd_string ="".join(new_string)
        return upd_string    
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
