#!/usr/bin/python3
def roman_to_int(roman_string):
    """ converts from roman numerals to integers """

    if roman_string is None or type(roman_string) is not str:
        return (0)

    rom_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    roman_str = list(roman_string.upper())
    result = 0
    prev = 0

    for letter in roman_str:
        if letter in rom_to_int:
            result += rom_to_int[letter]
            if rom_to_int[letter] > prev:
                result -= prev * 2
            prev = rom_to_int[letter]
        else:
            return (0)
    return (result)
