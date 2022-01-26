#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 26 Janvier 2022 14:28
"""


def deci_bin(entier: int) -> str:
    res = ""
    while entier > 0:
        res = str(entier % 2)+res
        entier = entier//2
    return res


def decoder(code_car: list) -> str:
    res = ""
    for code in code_car:
        res = res+chr(code)
    return res


print(deci_bin(11))
print(decoder([83, 65, 76, 85, 84]))
