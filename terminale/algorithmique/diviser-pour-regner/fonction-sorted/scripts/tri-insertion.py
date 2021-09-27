#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 26 Septembre 2021 20:42
"""

from random import randint
from time import time


def tri_insertion(tab: list) -> None:
    for i in range(len(tab)-1):
        j = i+1
        while j > 0 and tab[j] < tab[j-1]:
            tab[j], tab[j-1] = tab[j-1], tab[j]
            j -= 1


tab = [randint(1, 100) for _ in range(10)]
print(tab)
tri_insertion(tab)
print(tab)

tab2 = [randint(1, 10000) for _ in range(10000)]
deb = time()
tri_insertion(tab2)
fin = time()
print(fin-deb)
