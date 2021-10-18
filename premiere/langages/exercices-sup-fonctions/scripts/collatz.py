#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 18 Octobre 2021 12:24
"""


def collatz(n: int) -> bool:
    """
    renvoie True si la procédure termine
    Si la boucle ne se termine jamais, la conjecture
    est fausse.
    """
    while n != 1:
        if n % 2 == 0:  # pair
            n = n//2
        else:
            n = 3*n+1
    return True

print(collatz(6))