#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep 16 15:15:15 2020

@auteur: Christophe Viroulaud
"""


def C(n: int, p: int)->int:
    if p == 0 or n == p:
        return 1
    else:
        return C(n-1, p-1) + C(n-1, p)

for n in range(10):
    for p in range(n+1):
        print(C(n, p), end=" ")
    print()