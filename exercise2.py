#!/usr/bin/env python3

"""Assignment 1, Exercise 2, INF1340, Fall 2014. UPC Checksum.

This module contains one function, checksum.

It can be passed a string of 12 digits. All
other inputs will result in an error.

Example:
    $ python exercise2.py

"""

__author__ = "Joshua Chisholm and Christopher Piche"
__email__ = "josh.chisholm@mail.utoronto.ca and christopher.piche@mail.utoronto.ca"

__copyright__ = "2014 Joshua Chisholm and Christopher Piche"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def checksum(upc):
    """
    Checks if the digits in a UPC are consistent with checksum

    :param:
        upc(integer): universal product code to verify correctness of digits
            Accepted values are 12 digits long, containing numbers 0 to 9

    :return:
        Boolean: True, checksum is correct
        False, otherwise

    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under)
        ValueError if string contains any character other than numbers 0 to 9

    """

    # check type of input
    # raise TypeError if not string
    if not type(upc) == str:
        raise TypeError("Entered UPC must be a string")

    # check contents of input
    # raise ValueError if there are non-digit characters
    if not upc.isdigit():
        raise ValueError("Entered UPC must contain digits only")

    # check length of string
    # raise ValueError if length of upc is not 12 digits
    if not len(upc) == 12:
        digit_difference = len(upc) - 12
        if digit_difference < 0:
            raise ValueError("Entered UPC must be 12 digits; you are under by " + str(abs(digit_difference)) + " digits")
        else:
            raise ValueError("Entered UPC must be 12 digits; you are over by " + str(digit_difference) + " digits")

    even_sum = 0
    odd_sum = 0
    count = 0

    for digit in upc[:-1]:
        if count % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
        count += 1

    # generate checksum using the first 11 digits provided
    result = (((even_sum * 3) + odd_sum) % 10)

    if not result == 0:
        result = 10 - result

    # check against the the twelfth digit
    return result == int(upc[-1])

