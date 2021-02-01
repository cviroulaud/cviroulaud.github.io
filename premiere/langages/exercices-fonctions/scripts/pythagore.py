#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 15:15:27 2021

@auteur: Christophe Viroulaud
"""


def pythagore(a: int, b: int, c: int)->bool:
    """
    vérifie si le triangle a, b, c est rectangle

    Parameters
    ----------
    a, b, c: int
        mesures des côtés.

    Returns
    -------
    Boolean.

    """
    return a**2 + b**2 == c**2

print(pythagore(3, 4, 5))
