#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 23 Janvier 2022 09:13
"""



def xor(x: bool, y: bool) -> bool:
    return (x and not y) or (not x and y)


print(xor(False, False))
print(xor(False, True))
print(xor(True, False))
print(xor(True, True))
