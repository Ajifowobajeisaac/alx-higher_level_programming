#!/usr/bin/python3

import sys



if __name__ == "__main__":
    args = sys.argv
    args_int = [int(arg) for arg in args[1:]]
    args_sum = sum(args_int)
    print(args_sum)
