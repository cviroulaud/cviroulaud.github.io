#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 14 Avril 2022 17:32
"""


def int_bin(nb: int) -> list:
    if nb == 0:
        return []
    return int_bin(nb//2)+[nb % 2]


print(int_bin(10))
