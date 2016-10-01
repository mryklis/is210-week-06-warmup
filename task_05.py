#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""this module inverts the sequence of a list"""


def flip_keys(to_flip):
    """reverses the order of objects in the inner list

    Args:
        to_flip (list): a list with an inner list.

    Returns:
        to_flip (list): with inner objects in reverse order.

    Example:
        >>>LIST = [(1, 2, 3), 'abc']
        >>>NEW = flip_keys(LIST)
        >>>print LIST
        [(3, 2, 1), 'cba']
    """

    counter = 0
    for obj in to_flip:
        obj = to_flip[counter][::-1]
        to_flip[counter] = obj
        counter += 1
    return to_flip
