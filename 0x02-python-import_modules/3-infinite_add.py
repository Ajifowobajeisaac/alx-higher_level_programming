#!/usr/bin/python3

import sys

args = sys.argv

args_int = [int(arg) for arg in args[1:]]
print(sum(args_int))
