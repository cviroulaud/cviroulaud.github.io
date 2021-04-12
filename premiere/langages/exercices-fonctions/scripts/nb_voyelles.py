#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 16:12:10 2021

@auteur: Christophe Viroulaud
"""


def nb_voyelles(mot: str)->int:
    """
    renvoie le nombre de voyelles dans mot
    """
    voyelles = ["a","e","i","o","u","y"]
    nb = 0
    for c in mot:
        if c in voyelles:
            nb += 1
    return nb

print(nb_voyelles("eeerru"))
