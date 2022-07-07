#!/usr/bin/python3
def search_replace(my_list, search, replace):
    upd_list = my_list.copy()
    for i in range(len(upd_list)):
        if upd_list[i] == search:
            upd_list[i] = replace
    return upd_list
