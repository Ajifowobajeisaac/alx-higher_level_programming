#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	sorted_dict = sorted(a_dictionary.keys())
	for k in sorted_dict:
            print("{}: {}".format(k, a_dictionary[k]))
