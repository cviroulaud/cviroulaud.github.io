#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/08/29 14:17:33
"""

n = int(input("Entrer un entier positif: "))
res = ""
while (n > 0):
    res = str(n % 2)+res
    n = n//2
print(res)
