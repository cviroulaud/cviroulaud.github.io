#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 17 Octobre 2021 14:40
"""

from random import randint

tab = [randint(0, 100) for i in range(10)]

def maxi(tab: list) -> int:
    maximum = 0
    for element in tab:
        if element > maximum:
            maximum = element
    return maximum

print(tab)
print(maxi(tab))