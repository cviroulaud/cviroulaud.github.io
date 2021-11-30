#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 27 Novembre 2021 23:04
"""

#DODO faire avec celui-ci?
def exporapide(a, n):
    if n == 0:
        return 1
    b = exporapide(a, n//2)
    if (n % 2) == 1:
        return b*b*a
    else:
        return b*b
