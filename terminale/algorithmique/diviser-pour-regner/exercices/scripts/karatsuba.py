#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/09/10 10:49:42
"""


def kara(m1: int, m2: int, n: int) -> int:
    if n == 1:
        return m1*m2
    else:
        k = n//2
        a = m1//10**k
        b = m1 % 10**k
        c = m2//10**k
        d = m2 % 10**k
        a0 = kara(a, c, n//2)
        a2 = kara(b, d, n//2)
        a1 = kara(a-b, c-d, n//2)
        return a0*10**(2*k)+(a0+a2-a1)*10**k+a2

print(kara(1237,2587,4))
print(kara(123,2587,4))