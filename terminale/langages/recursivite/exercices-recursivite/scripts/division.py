#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/07/30 22:54:39
"""


def division(dividende: int, diviseur: int) -> tuple:
    quotient = 0
    while dividende >= diviseur:
        quotient += 1
        dividende -= diviseur
    return (quotient, dividende)


def division_rec(dividende: int, diviseur: int) -> tuple:
    if dividende < diviseur:
        return (0, dividende)
    else:
        res = division_rec(dividende-diviseur, diviseur)
        return (1+res[0], res[1])


print(division(23, 5))
print(division_rec(23, 5))
print(division(25, 5))
print(division_rec(25, 5))
