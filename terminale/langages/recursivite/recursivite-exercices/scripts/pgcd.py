#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep 16 14:46:56 2020

@auteur: Christophe Viroulaud
"""


def pgcd(a: int, b: int)->int:
    if a == 0:
        return b
    else:
        return pgcd(b%a, a)

print(pgcd(20,35))