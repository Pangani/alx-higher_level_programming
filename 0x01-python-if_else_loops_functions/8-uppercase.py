#!/usr/bin/python3

def uppercase(str):
    for c in str:
        charac = ord(c)
        if charac >= 97 and charac <= 122:
            charac -= 32
        print("{:c}".format(charac), end="")
    print()
