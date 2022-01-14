#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 12 Janvier 2022 17:16
"""


def dec_bin(nb: int) -> list:
    binaire = [0 for _ in range(8)]
    for i in range(7, -1, -1):
        binaire[i] = nb % 2
        nb = nb//2
    return binaire


def IP_bin(ip: list) -> list:
    return [dec_bin(ip[i]) for i in range(4)]


print(dec_bin(10))
print(dec_bin(255))
print(IP_bin([192, 168, 0, 1]))
