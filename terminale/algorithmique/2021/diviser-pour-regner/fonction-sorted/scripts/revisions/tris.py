#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 04 Mars 2022 12:07
"""

from random import randint


def tri_rapide(tab: list, deb: int, fin: int) -> None:
    if fin > deb:
        pivot = tab[deb]
        pos_piv = deb
        for i in range(deb+1, fin+1):
            if tab[i] < pivot:
                tab[i], tab[pos_piv+1] = tab[pos_piv+1], tab[i]
                tab[pos_piv], tab[pos_piv+1] = tab[pos_piv+1], tab[pos_piv]
                pos_piv = pos_piv+1
        tri_rapide(tab, deb, pos_piv-1)
        tri_rapide(tab, pos_piv+1, fin)


l = [randint(0, 100) for _ in range(20)]
print(l)
tri_rapide(l, 0, len(l)-1)
print(l)


def fusionner(tab: list, deb: int, fin: int) -> None:
    m = (fin+deb)//2
    i = deb
    j = m+1
    temp = []
    while i <= m and j <= fin:
        if tab[i] < tab[j]:
            temp.append(tab[i])
            i = i+1
        else:
            temp.append(tab[j])
            j = j+1
    for k in range(i, m+1):
        temp.append(tab[k])
    for k in range(j, fin+1):
        temp.append(tab[k])
    for k in range(len(temp)):
        tab[k+deb] = temp[k]


def tri_fusion(tab: list, deb: int, fin: int) -> None:
    if fin > deb:
        m = (fin+deb)//2
        tri_fusion(tab, deb, m)
        tri_fusion(tab, m+1, fin)
        fusionner(tab, deb, fin)

l = [randint(0, 100) for _ in range(20)]
print(l)
tri_fusion(l, 0, len(l)-1)
print(l)