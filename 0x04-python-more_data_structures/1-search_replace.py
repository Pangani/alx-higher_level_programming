#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for elem in range(len(new_list)):
        if new_list[elem] == search:
            new_list[elem] = replace
    return new_list
