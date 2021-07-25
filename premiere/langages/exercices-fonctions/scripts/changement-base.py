#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/06/30 14:45:04
"""


def dec_to_bin(x: int) -> str:
    """
    >>> dec_to_bin(35)
    '100011'

    """
    res = ''
    while x > 0:
        res = str(x % 2)+res
        x //= 2
    return res


def dec_to_bin_rec(x: int) -> str:
    """
    >>> dec_to_bin_rec(35)
    '100011'

    """
    if x == 1:
        return str(x)
    else:
        return dec_to_bin_rec(x//2)+str(x % 2)


def conversion(x: int, base: int) -> str:
    """
    >>> conversion(1830, 16)
    '726'

    >>> conversion(35,2)
    '100011'
    """
    if x < base:
        return str(x)
    else:
        return conversion(x//base, base)+str(x % base)


def horner(x: str) -> int:
    """
    >>> horner('100011')
    35
    """
    res = 0
    while len(x) > 0:
        res = res*2+int(x[0])
        x = x[1:]
    return res


def horner_rec(x: str) -> int:
    """
    >>> horner_rec('100011')
    35
    """
    if len(x) == 1:
        return int(x[0])
    else:
        return horner_rec(x[:-1])*2+int(x[-1])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
