#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 15:38:12 2021

@auteur: Christophe Viroulaud
"""


def puissance(x: int, n: int)->int:
    """
    élève x à la puissance n

    Parameters
    ----------
    x : int
        entier.
    n : int
        exposant.

    Returns
    -------
    res : int
    """
    res = 1
    for i in range(n):
        res *= x
    return res

print(puissance(3, 4))
