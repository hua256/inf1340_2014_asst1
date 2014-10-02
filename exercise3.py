#!/usr/bin/env python3

"""Assignment 1, Exercise 3, INF1340, Fall 2014. Rock, Paper, Scissors.

This module contains one function XXXX.

It can be passed XXXX. All
other inputs will result in an error.

Example:
    $ python exercise3.py

"""

__author__ = "Joshua Chisholm and Christopher Piche"
__email__ = "josh.chisholm@mail.utoronto.ca and christopher.piche@mail.utoronto.ca"

__copyright__ = "2014 Joshua Chisholm and Christopher Piche"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def rpc_result(upc):
    """
    Checks if the digits in a UPC are consistent with checksum

    :param
        upc(integer): universal product code to verify correctness of digits
            Accepted values are

    :return:
        Boolean: True, checksum is correct
        False, otherwise

    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under

    """

    # check type of input
    # raise TypeError if not string

    # check length of string
    # raise ValueError if not 12

    # convert string to array
    # hint: use the list function

    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit

    # return True if they are equal, False otherwise


rps_results[("Rock", "Paper")] = 2
rps_results[("Paper", "Rock")] = 1
rps_results[("Scissors", "Rock")] = 2
rps_results[("Scissors", "Paper")] = 1
rps_results[("Rock", "Scissors")] = 1
rps_results[("Scissors", "Rock")] = 2
rps_results[("Scissors", "Paper")] = 1
rps_results[("Paper", "Scissors")] = 2
rps_results[("Rock", "Rock")] = 0
rps_results[("Paper", "Paper")] = 0
rps_results[("Scissors", "Scissors")] = 0



    return False


#!/usr/bin/env python3


def decide_rps(player1, player2):
    result_output = {"Player 1": 1, "Player 2": 2, "Tie": 0}




    return 1

