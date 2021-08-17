#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/07/09 16:05:38
"""


def division_rec(dividende: int, diviseur: int) -> tuple:
    if dividende < diviseur:
        return (0, dividende)
    t = division_rec(dividende-diviseur, diviseur)
    return (t[0]+1, t[1])


print(division_rec(39, 5))
print(division_rec(35, 5))


def division(dividende: int, diviseur: int) -> tuple:
    q = 0
    while dividende >= diviseur:
        q += 1
        dividende -= diviseur
    return (q, dividende)


print(division(39, 5))
print(division(35, 5))
