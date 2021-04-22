#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/20 21:18:14
"""


def int_en_bin(nb: int) -> str:
    """
    Convertit un entier en sa représentation binaire
    """
    q = nb
    r = ""
    while q > 0:
        r = str(q % 2)+r
        q = q//2
    return r


def bin_en_int(paquet: str) -> int:
    """
    Convertit un paquet de bits en entier
    """
    entier = 0
    for i in range(len(paquet)):
        entier += int(paquet[i])*2**(len(paquet)-1-i)
    return entier


print(int_en_bin(66))
print(int_en_bin(82))
print(int_en_bin(65))
print(int_en_bin(86))
print(int_en_bin(79))
print(int_en_bin(78))
print(int_en_bin(83))
print(int_en_bin(73))

print(bin_en_int("0001100"))
print(bin_en_int("0000001"))
print(bin_en_int("0001000"))
print(bin_en_int("0011000"))
print(bin_en_int("0011100"))

