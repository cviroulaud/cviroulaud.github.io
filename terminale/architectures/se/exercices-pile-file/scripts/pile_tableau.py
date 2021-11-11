#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 19 Octobre 2021 09:04
"""

from random import randint


def creer_pile() -> list:
    return []


def est_vide(p: list) -> bool:
    return len(p) == 0


def empiler(p: list, e: int) -> None:
    p.append(e)


def depiler(p: list) -> int:
    if not est_vide(p):
        return p.pop()
    raise IndexError("pile vide")


p = creer_pile()
for i in range(5):
    empiler(p, randint(0, 10))
    print("empiler ", p)

while not est_vide(p):
    print("dépiler ", p, "->", depiler(p))

depiler(p)
