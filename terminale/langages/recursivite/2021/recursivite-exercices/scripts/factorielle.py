#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep 16 14:00:17 2020

@auteur: Christophe Viroulaud
"""


def factorielle(n: int)->int:
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

print(factorielle(10))