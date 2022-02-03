#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 02 Février 2022 10:59
"""


def images(deb, fin: int) -> list:
    """
    calcule les images d'une fonction
    """
    tab = []
    for i in range(deb, fin):
        tab.append(f(i))
    return tab


def f(x: int) -> int:
    return 1/x


if __name__ == "__main__":
    print(images(1, 5))
