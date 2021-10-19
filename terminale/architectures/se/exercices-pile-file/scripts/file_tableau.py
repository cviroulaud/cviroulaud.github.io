#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 19 Octobre 2021 09:04
"""

from random import randint


def est_vide(f: list) -> bool:
    return len(f) == 0


def enfiler(f: list, e: int) -> None:
    f.insert(0, e)


def defiler(f: list) -> int:
    return f.pop()


f = []
for i in range(5):
    enfiler(f, randint(0, 10))
    print("enfiler ->", f)

while not est_vide(f):
    print("défiler ", f, "->", defiler(f))
