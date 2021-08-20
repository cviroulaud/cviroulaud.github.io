#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/07/29 15:21:50
"""


def nb_chiffres(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1+nb_chiffres(n//10)


def nb_chiffres_terminal(n: int, acc: int) -> int:
    if n < 10:
        return acc
    else:
        return nb_chiffres_terminal(n//10, acc+1)


print(nb_chiffres(1234))
print(nb_chiffres_terminal(1234, 1))
