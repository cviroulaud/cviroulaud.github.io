#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/22 09:31:03
"""
import sys
sys.setrecursionlimit(20000)
COMPTEUR = 0


def puissance_perso(x: int, n: int) -> int:
    global COMPTEUR
    res = 1
    for i in range(n):
        COMPTEUR += 1
        res *= x
    return res


def puissance_recursif(x: int, n: int) -> int:
    global COMPTEUR
    if n == 0:
        return 1
    else:
        COMPTEUR += 1
        return x*puissance_recursif(x, n-1)


def puissance_recursif_rapide(x, n):
    global COMPTEUR
    if n == 0:
        return 1
    elif n % 2 == 0:
        COMPTEUR += 1
        return puissance_recursif_rapide(x*x, n//2)
    else:
        COMPTEUR += 1
        return x*puissance_recursif_rapide(x*x, n//2)


def puissance_iteratif_rapide(x, n):
    global COMPTEUR
    res = 1
    while n > 0:
        COMPTEUR += 1
        if n % 2 != 0: #impair
            res = res * x
        x = x*x
        n = n//2
    return res


puissance_perso(2701, 19406)
print("perso: ", COMPTEUR)

COMPTEUR = 0
puissance_recursif(2701, 19406)
print("récursif: ", COMPTEUR)

COMPTEUR = 0
puissance_recursif_rapide(2701, 19406)
print("récursif rapide: ", COMPTEUR)

COMPTEUR = 0
puissance_iteratif_rapide(2701, 19406)
print("itératif rapide: ", COMPTEUR)

