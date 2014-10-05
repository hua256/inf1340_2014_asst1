#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall 2014. Grade-to-GPA conversion.

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = "Joshua Chisholm and Christopher Piche"
__email__ = "josh.chisholm@mail.utoronto.ca and christopher.piche@mail.utoronto.ca"

__copyright__ = "2014 Joshua Chisholm an Christopher Piche"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100
            If string, accepted values are A+, A, A-, B+, B, B-, or FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range

    """

    letter_grade = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "FZ": 0.0}

    if type(grade) is str:
        # check that the grade is one of the accepted values
        # assign grade to letter_grade
        # convert input to upper case

        grade = grade.upper()

        # check that the grade is in letter_grade dictionary

        try:
            gpa = letter_grade[grade]
        except:
            # raise a Value Error exception
            raise ValueError("Entered grade must fall within U of T grad student grading scale")

    elif type(grade) is int:
        # check that grade is in the accepted range
        # convert the numeric grade to a letter grade
        # assign the value to letter_grade

        if grade < 0:
            # raise a ValueError exception
            raise ValueError("Entered grade can not be less than 0")
        elif grade <= 69:
            gpa = 0.0
        elif grade <= 72:
            gpa = 2.7
        elif grade <= 76:
            gpa = 3.0
        elif grade <= 79:
            gpa = 3.3
        elif grade <= 84:
            gpa = 3.7
        elif grade <= 100:
            gpa = 4.0
        else:
            # raise a ValueError
            raise ValueError("Entered grade can not be greater than 100")


    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    return gpa