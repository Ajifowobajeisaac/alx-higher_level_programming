#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	sorted_dict = sorted(a_dictionary.keys())
	for i in sorted_dict:
            value = a_dictionary[i]
            print("{}: {}".format(i, value))
