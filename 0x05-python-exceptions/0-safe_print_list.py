#!/usr/bin/python3
"""
    safe_print_list - prints list of any type
    @x: number of elements to print
    return: number of elem printed """


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except Exception:
            continue
    print()
    return count
