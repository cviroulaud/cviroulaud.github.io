#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/07/29 15:21:50
"""


def nombre_chiffres(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + nombre_chiffres(n//10)


def nombre_chiffres_terminal(n: int, acc: int) -> int:
    if n < 10:
        return acc
    else:
        return nombre_chiffres_terminal(n//10, acc+1)


print(nombre_chiffres(1234))
print(nombre_chiffres_terminal(1234, 1))
