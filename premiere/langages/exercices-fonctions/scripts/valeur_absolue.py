#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 15:06:24 2021

@auteur: Christophe Viroulaud
"""


def valeur_absolue(x: int)->int:
    """
    renvoie la valeur absolue de x
    """
    if x < 0:
        return -x
    else:
        return x
