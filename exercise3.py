#!/usr/bin/env python3

"""Assignment 1, Exercise 3, INF1340, Fall 2014. Rock, Paper, Scissors.

This module contains one function rps_result.

It should be passed a parameter that is a string from both Player 1 and Player 2 (Rock, Paper, Scissors). All
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

def rps_results(Player1, Player2):
    """
    Returns the result of Rock, Paper, Scissors games given each player's choice.

    :param:
        (str, str) -> int : the result to be confirmed
            Accepted values are Rock, Paper, Scissors

    :return:
        Integer: the game result
            Value is 0 (tie), 1 (Player1 wins), or 2 (Player2 wins)

    :raises:
        TypeError if input is not a string
        ValueError if string is not in dictionary

    """

    # check type of input
    # raise TypeError if not string
    # error will be raised for either player
    if not type(Player1) == str:
        raise TypeError("Entered value must be a string")

    # check type of input
    # raise TypeError if not string
    # error will be raised for either player
    if not type(Player2) == str:
        raise TypeError("Entered value must be a string")

    # capitalize first letter of choice to avoid error
    Player1 = Player1.title()
    Player2 = Player2.title()

    # check value of input
    # raise ValueError if value not in dictionary
    # error will be raised for either player
    if not Player1 in ("Rock", "Paper", "Scissors"):
        raise ValueError("Entered moves must be Rock, Paper, or Scissors for each player")

    # check value of input
    # raise ValueError if value not in dictionary
    # error will be raised for either player
    if not Player2 in ("Rock", "Paper", "Scissors"):
        raise ValueError("Entered move must be Rock, Paper, or Scissors for each player")

    # build dictionary for all possible results
    rps_results={}
    rps_results[("Rock", "Paper")] = 2
    rps_results[("Rock", "Scissors")] = 1
    rps_results[("Paper", "Rock")] = 1
    rps_results[("Paper", "Scissors")] = 2
    rps_results[("Scissors", "Rock")] = 2
    rps_results[("Scissors", "Paper")] = 1
    rps_results[("Rock", "Rock")] = 0
    rps_results[("Paper", "Paper")] = 0
    rps_results[("Scissors", "Scissors")] = 0

    # return winner based on player parameters
    return rps_results[Player1, Player2]

