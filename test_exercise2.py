#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = "Joshua Chisholm and Christopher Piche"
__email__ = "josh.chisholm@mail.utoronto.ca and christopher.piche@mail.utoronto.ca"

__copyright__ = "2014 Joshua Chisholm an Christopher Piche"
__license__ = "MIT License"

__status__ = "Prototype"

import pytest
from exercise2 import checksum

def test_checksum():
    """
    Test some UPCs to insure the results are coming out correctly
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("639382000393") is True
    assert checksum("123456789012") is True
    assert checksum("763089537613") is True
    assert checksum("653100976548") is True
    assert checksum("000000000000") is True
    assert checksum("000213035158") is True
    assert checksum("010608030606") is True
    assert checksum("407020803091") is True
    assert checksum("717951000841") is False
    assert checksum("085392132220") is False
    assert checksum("639382000396") is False
    assert checksum("123456789011") is False
    assert checksum("763089537617") is False
    assert checksum("653100976549") is False
    assert checksum("000000000001") is False
    assert checksum("000213035154") is False
    assert checksum("010608030609") is False
    assert checksum("407020803092") is False

def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0) # no floats allowed
        checksum(786936224306.0) # no floats allowed
        checksum(786936224306) # no ints allowed
        checksum((7,8,6,9,3,6,2,2,4,3,0,6)) # no lists allowed

    with pytest.raises(ValueError):
        checksum("") # must not be less than 12 characters
        checksum("1") # must not be less than 12 characters
        checksum("1234567890") # must not be less than 12 characters
        checksum("1234567890123123557") # must not be more than 12 characters
        checksum("40702080309a") # must not contain a character
        checksum("763O895376l7") # must not contain the letters 'O' and 'l'
        checksum("abcdefghijkl") # must not contain only characters
