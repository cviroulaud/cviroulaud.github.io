#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/18 10:14:19
"""

from random import randint

somme = 0
for i in range(10):
    nb = randint(1, 10)
    somme += nb
print(somme)
