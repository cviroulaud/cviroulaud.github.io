#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 26 Janvier 2022 14:51
"""


def utf8(car: str) -> str:
    return hex(ord(car))


def encoder_hexa(phrase: str) -> list:
    codes = []
    for lettre in phrase:
        codes.append(utf8(lettre))
    return codes


def encoder_hexa2(phrase: str) -> list:
    codes = ["" for _ in range(len(phrase))]
    for i in range(len(phrase)):
        codes[i] = utf8(phrase[i])
    return codes


print(utf8("é"))
print(encoder_hexa("éléphant"))
print(encoder_hexa2("éléphant"))
