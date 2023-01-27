#!/usr/bin/python3
"""Reads from input and compute metrics

After every 10 lines and keyboard interruption
prints:
    -total file size
    - count of read codes
"""


def show_stats(size, status_code):
    """Print accumulated metrics.
    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    possible_status_codes = ['200', '301', '400', '403', '404', '405', '500']
    count = 0

try:
    for line in sys.stdin:
        if count == 10:
            show_stats(size, status_code)
            count = 1
        else:
            count += 1

        line = line.split()

        try:
            size += int(line[-1])
        except (IndexError, ValueError):
            pass

        try:
            if line[-2] in possible_status_codes:
                if status_code.get(line[-2], -1) == -1:
                    status_code[line[-2]] = 1
                else:
                    status_code[line[-2]] += 1
        except IndexError:
            pass

except KeyboardInterrupt:
    show_stats(size, status_code)
    raise
