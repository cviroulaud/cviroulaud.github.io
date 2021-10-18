#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 18 Octobre 2021 09:12
"""


def volume(long: int, larg: int, haut: int) -> int:
    """
    renvoie le volume d'un pavé

    Args:
        long (int): longueur
        larg (int): largeur
        haut (int): hauteur

    Returns:
        int: volume
    """
    return long*larg*haut

print(volume(3, 4, 5))