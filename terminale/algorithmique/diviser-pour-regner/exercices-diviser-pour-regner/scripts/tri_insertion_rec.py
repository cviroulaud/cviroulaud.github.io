#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 30 Septembre 2021 23:22
"""
from random import randint

def inserer(tab: list, j: int) -> None:
    if j >= 0 and tab[j] > tab[j+1]:
        tab[j], tab[j+1] = tab[j+1], tab[j]
        inserer(tab, j-1)


def tri_insertion_rec(tab: list) -> None:
    for i in range(len(tab)):
        inserer(tab, i-1)
        
t = [randint(1,100) for _ in range(10)]
print(t)
tri_insertion_rec(t)
print(t)