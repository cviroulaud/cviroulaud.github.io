#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 26 Septembre 2021 20:20
"""
from random import randint
from time import time


def tri_selection(tab: list) -> None:
    for i in range(len(tab)):
        i_mini = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[i_mini]:
                i_mini = j
        tab[i], tab[i_mini] = tab[i_mini], tab[i]


tab = [randint(1, 100) for _ in range(10)]
print(tab)
tri_selection(tab)
print(tab)

tab2 = [randint(1, 10000) for _ in range(10000)]
deb = time()
tri_selection(tab2)
fin = time()
print("sélection ",fin-deb)

tab2 = [randint(1, 10000) for _ in range(10000)]
deb = time()
tab2.sort()
fin = time()
print("sort ",fin-deb)
