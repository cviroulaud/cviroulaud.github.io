#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 15:11:39 2021

@auteur: Christophe Viroulaud
"""

from math import pi

def surface2(r: int) -> float:
    """
    renvoie la surface du disque de rayon r
    utilise la bibliothèque math
    """
    return pi*r**2

print(surface2(5))

def surface(r: int) -> float:
    """
    renvoie la surface du disque de rayon r
    """
    return 3.14*r**2

print(surface(5))
