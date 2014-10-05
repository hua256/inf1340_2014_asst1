#!/usr/bin/env python3

""" Module to test exercise3.py """

__author__ = "Joshua Chisholm and Christopher Piche"
__email__ = "josh.chisholm@mail.utoronto.ca and christopher.piche@mail.utoronto.ca"

__copyright__ = "2014 Joshua Chisholm and Christopher Piche"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

import pytest
from exercise3 import rps_results


def test_rps_results():
    """
    Confirm that all results are true as asserted
    """

    assert rps_results("Rock", "Paper") == 2
    assert rps_results("Rock", "Scissors") == 1
    assert rps_results("Paper", "Rock") == 1
    assert rps_results("Paper", "Scissors") == 2
    assert rps_results("Scissors", "Rock") == 2
    assert rps_results("Scissors", "Paper") == 1
    assert rps_results("Rock", "Rock") == 0
    assert rps_results("Paper", "Paper") == 0
    assert rps_results("Scissors", "Scissors") == 0

def test_input():
    """
    Inputs are not correct type and contents
    """
    with pytest.raises(TypeError):
        rps_results(1.0, "Rock") # no floats allowed
        rps_results("Rock", 1.0) # no floats allowed
        rps_results(2, "Scissors") # no ints allowed
        rps_results("Scissors", 2) # no int allowed

    with pytest.raises(ValueError):
        rps_results("", "Rock") # entered values must be Rock, Paper, or Scissors for both
        rps_results("Paper", "S") # entered values must be Rock, Paper, or Scissors for both
        rps_results("R0ck", "P4p3r") # must not contain a digit


