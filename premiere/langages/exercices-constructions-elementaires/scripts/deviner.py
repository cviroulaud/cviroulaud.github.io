#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/18 10:18:38
"""

from random import randint

nb = randint(1,10)
essai = 1
while not(int(input("Quel nombre? ")) == nb):
    essai += 1
print(essai)