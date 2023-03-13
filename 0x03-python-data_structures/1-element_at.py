#!/usr/bin/python3
def element_at(my_list, idx):
    for item in my_list:
        if idx > len(my_list) - 1:
            return None
        elif idx < 0:
            return None
        else:
            return my_list[idx]
