#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep 16 14:46:56 2020

@auteur: Christophe Viroulaud
"""


def pgcd(a: int, b: int) -> int:
    while a != 0:
        a, b = b % a, a
    return b


def pgcd_rec(a: int, b: int) -> int:
    if a == 0:
        return b
    else:
        return pgcd_rec(b % a, a)


print(pgcd(20, 35))
print(pgcd_rec(20, 35))
