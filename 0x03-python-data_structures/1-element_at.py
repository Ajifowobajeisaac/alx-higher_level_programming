#!/usr/bin/python3

"""Retrieves an element from a list at a specific index"""


def element_at(my_list, idx):
    """Retrieves an element from a list at a specific index"""
    if my_list:
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            return my_list[idx]
