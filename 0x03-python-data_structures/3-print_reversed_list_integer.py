#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = 0
    for item in my_list:
        if idx < len(my_list):
            idx -= 1
            print('{:d}'.format(my_list[idx]))
