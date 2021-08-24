#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep 16 14:34:29 2020

@auteur: Christophe Viroulaud
"""


def entiers(i: int, k: int) -> None:
    if i <= k:
        print(i, end=" ")
        entiers(i+1, k)


entiers(0, 3)

print()


def impairs(i: int, k: int) -> None:
    if i <= k:
        if i % 2 == 1:
            print(i, end=" ")
        impairs(i+2, k)


impairs(1, 8)
