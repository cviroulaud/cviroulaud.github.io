#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 06 Octobre 2021 11:39
"""

from random import randint


def lancer_des() -> int:
    """
    renvoie la somme de deux dés
    """
    de1 = randint(1, 6)
    de2 = randint(1, 6)
    return de1+de2
