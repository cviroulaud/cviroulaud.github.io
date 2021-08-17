#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 16:00:08 2021

@auteur: Christophe Viroulaud
"""


def nombres_pairs(x: int)->list:
    """
    renvoie la liste des nombres pairs < x
    """
    return[i for i in range(0,x,2)]

print(nombres_pairs(10))
