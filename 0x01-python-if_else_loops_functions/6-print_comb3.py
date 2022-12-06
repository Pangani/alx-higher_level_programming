#!/usr/bin/python3

for dgt1 in range(0, 9):
    for dgt2 in range(dgt1 + 1, 10):
        if dgt1 == 8:
            print("{:d}{:d}".format(dgt1, dgt2))
            break
        print("{:d}{:d}".format(dgt1, dgt2), end=", ")
