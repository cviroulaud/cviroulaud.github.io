#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Jan  4 16:55:40 2021

@auteur: Christophe Viroulaud
"""


def division(a, b):
    q = 0
    r = a
    while r >= b:
        q += 1
        r -= b
    return (q, r)