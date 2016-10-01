#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module explores using lists and arithmetic operations"""


def process_data(data):
    """this function adds the items in a list and then divides by # of items.

    Arguments:
        data (list) = consists of numbers to summed and averaged

    Returns:
        sum (int) = the sum of the list items added to each other
        avg (float) = the sum divided by number of items in list

    Examples:
        >>>process_data([1, 2, 3])
        (6, 2.0)
    """

    total = 0
    for num in data:
        total += num
        avg = total/len(data)
    return total, float(avg)
