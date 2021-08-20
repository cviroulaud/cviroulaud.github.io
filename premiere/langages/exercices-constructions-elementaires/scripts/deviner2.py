#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/18 10:18:38
"""

from random import randint

nb = randint(1,10)
essai = 0
trouve = False
while not trouve:
    proposition = int(input("Quel nombre? "))
    if proposition == nb:
        trouve = True
    essai += 1
print(essai)