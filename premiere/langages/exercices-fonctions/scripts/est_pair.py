#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 05 Octobre 2021 22:15
"""


def est_pair(x: int) -> bool:
    """
    vérifie si x est pair

    Args:
        x (int): entier

    Returns:
        bool: True si x est pair
    """
    if x % 2 == 0:
        return True
    else:
        return False

# appel de la fonction
print(est_pair(5))
