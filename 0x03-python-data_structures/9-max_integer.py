#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = 0
    if my_list == "":
        return None
    for i in range(len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]
    return max_num
