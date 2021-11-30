#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 26 Novembre 2021 14:33
"""

import doctest


def calcul(n: int) -> list:
    """
    C'est la suite de syracuse

    Args:
        n (int): U0

    Returns:
        list: les éléments de la suite

    >>> calcul(7)
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    res = []
    while n != 1:
        res.append(n)
        if n % 2 == 0:
            n = n//2
        else:  # impair
            n = 3*n+1
    res.append(1)
    return res


def syracuse(n: int) -> list:
    """
    version récursive 

    >>> syracuse(7)
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if n != 1:
        if n % 2 == 0:
            return [n]+syracuse(n//2)
        else:  # impair
            return [n]+syracuse(3*n+1)
    else:
        return [1]


if __name__ == "__main__":
    doctest.testmod(verbose=True)
