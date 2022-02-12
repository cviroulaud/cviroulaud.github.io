#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/22 22:01:08

version tri en place
"""

from random import randint
from time import time


def fusionner(tab: list, deb: int, fin: int) -> None:
    res = [0 for _ in range(fin-deb+1)]
    milieu = (deb+fin)//2
    i = deb
    j = milieu+1
    k = 0
    while i <= milieu and j <= fin:
        if tab[i] < tab[j]:
            res[k] = tab[i]
            i += 1
        else:
            res[k] = tab[j]
            j += 1
        k += 1
    # ajout fin de tab
    for i1 in range(i, milieu+1):
        res[k] = tab[i1]
        k += 1
    for j1 in range(j, fin+1):
        res[k] = tab[j1]
        k += 1
    # remplacement tab par res
    for k in range(fin-deb+1):
        tab[deb+k] = res[k]


def tri_fusion(tab: list, deb: int, fin: int) -> None:
    if deb < fin:
        milieu = (deb+fin)//2
        tri_fusion(tab, deb, milieu)
        tri_fusion(tab, milieu+1, fin)
        fusionner(tab, deb, fin)


t = [randint(0, 100) for _ in range(10)]
print(t)
tri_fusion(t, 0, len(t)-1)
print(t)

tab2 = [randint(1, 10000) for _ in range(10000)]
deb = time()
tri_fusion(tab2, 0, len(tab2)-1)
fin = time()
print("fusion ", fin-deb)
