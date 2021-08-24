#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep 16 14:09:49 2020

@auteur: Christophe Viroulaud
"""


def syracuse2(u: int, l: list) -> list:
    l.append(u)
    if u > 1:
        if u % 2 == 0:
            syracuse2(u // 2, l)
        else:
            syracuse2(3 * u + 1, l)
    return l


print(syracuse2(5, []))


def syracuse(u: int) -> None:
    print(u, end=" ")
    if u > 1:
        if u % 2 == 0:
            syracuse(u // 2)
        else:
            syracuse(3 * u + 1)


syracuse(5)
