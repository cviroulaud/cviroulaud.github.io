#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 19 Octobre 2021 09:04
"""

from random import randint


def est_vide(p: list) -> bool:
    return len(p) == 0


def empiler(p: list, e: int) -> None:
    p.append(e)


def depiler(p: list) -> int:
    return p.pop()


p = []
for i in range(5):
    empiler(p, randint(0, 10))
    print("empiler ", p)

while not est_vide(p):
    print("dépiler ", p, "->", depiler(p))
