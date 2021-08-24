#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep 16 14:00:17 2020

@auteur: Christophe Viroulaud
"""


def somme(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + somme(n-1)


print(somme(10))


def somme_terminale(n: int, res: int) -> int:
    """
    version récursivité terminale
    """
    if n == 0:
        return res
    else:
        return somme_terminale(n-1, res+n)


print(somme_terminale(10, 0))
