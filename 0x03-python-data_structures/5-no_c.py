#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string"""

    upd_string = my_string
    del_string = upd_string
    remove_string = 'Cc'
    print(my_string.maketrans(upd_string, del_string, remove_string))
#     return upd_string    
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
