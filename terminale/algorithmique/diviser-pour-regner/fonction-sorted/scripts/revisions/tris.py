#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 16 Janvier 2022 22:28
"""
from random import randint


def tri_selection(l: list) -> None:
    for i in range(len(l)):
        i_mini = i
        for j in range(i, len(l)):
            if l[j] < l[i_mini]:
                i_mini = j
        l[i], l[i_mini] = l[i_mini], l[i]


def tri_insertion(l: list) -> None:
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j = j-1


def tri_bulle(l: list) -> None:
    for i in range(len(l)):
        for j in range(1, len(l)-i):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]


def fusionner(l: list, deb: int, fin: int) -> None:
    tab = [0 for _ in range(fin-deb+1)]
    milieu = (deb+fin)//2
    i, j, k = deb, milieu+1, 0
    while i <= milieu and j <= fin:
        if l[i] < l[j]:
            tab[k] = l[i]
            i = i+1
        else:
            tab[k] = l[j]
            j = j+1
        k = k+1

    for i1 in range(i, milieu+1):
        tab[k] = l[i1]
        k = k+1

    for j1 in range(j, fin+1):
        tab[k] = l[j1]
        k = k+1

    for i in range(len(tab)):
        l[i+deb] = tab[i]


def tri_fusion(l: list, deb: int, fin: int) -> None:
    if deb < fin:
        milieu = (deb+fin)//2
        tri_fusion(l, deb, milieu)
        tri_fusion(l, milieu+1, fin)
        fusionner(l, deb, fin)


def tri_rapide(l: list, deb: int, fin: int) -> None:
    if deb < fin:
        pos = deb
        pivot = l[pos]
        for i in range(deb+1, fin+1):
            if l[i] < pivot:
                l[pos] = l[i]
                l[i] = l[pos+1]
                l[pos+1] = pivot
                pos = pos+1
        tri_rapide(l, deb, pos-1)
        tri_rapide(l, pos+1, fin)


def tri_rapide2(l: list) -> list:
    if len(l) == 0:
        return []
    else:
        gauche = [l[i] for i in range(1, len(l)) if l[i] < l[0]]
        droite = [l[i] for i in range(1, len(l)) if l[i] >= l[0]]
        return tri_rapide2(gauche)+[l[0]]+tri_rapide2(droite)


tab = [randint(0, 100) for _ in range(20)]
print(tab)
print("tri rapide moche ", tri_rapide2(tab))


def test(tri, rec: bool = False):
    tab = [randint(0, 100) for _ in range(20)]
    if not rec:
        tri(tab)
    else:
        tri(tab, 0, len(tab)-1)
    print(tri.__name__)
    print(tab)


test(tri_selection)
test(tri_insertion)
test(tri_bulle)
test(tri_fusion, True)
test(tri_rapide, True)
