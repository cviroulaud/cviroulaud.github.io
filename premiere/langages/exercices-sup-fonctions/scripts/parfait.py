#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 18 Octobre 2021 09:16
"""


def est_parfait(n: int) -> bool:
    """
    vérifie si n est parfait
    """
    somme = 0
    for i in range(1, n):
        if n % i == 0:  # i est multiple de n
            somme += i
    # la somme des multiples == n
    return somme == n


print(est_parfait(6))
print(est_parfait(5))
print(est_parfait(28))
