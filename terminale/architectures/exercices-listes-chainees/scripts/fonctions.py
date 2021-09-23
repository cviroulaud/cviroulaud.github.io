#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 21 Septembre 2021 12:52
"""
from Liste import Liste, Maillon


def last(m: Maillon) -> int:
    if m.prec is None:
        return m.val
    return last(m.prec)


def two_last(m: Maillon) -> tuple:
    if m.prec is None:
        return m.val
    remontee = two_last(m.prec)
    if type(remontee) == int:
        return (m.val, remontee)
    else:
        return remontee


def k_ieme(m: Maillon, k: int) -> int:
    def aux(m: Maillon, k: int, i: int) -> int:
        if i == k:
            return m.val
        try:
            return aux(m.prec, k, i+1)
        except AttributeError:
            return -1

    res = aux(m, k, 0)
    if res < 0:
        return "k trop grand"
    else:
        return res


def longueur(m: Maillon) -> int:
    def aux(m: Maillon, i: int) -> int:
        if m is None:
            return i
        return aux(m.prec, i+1)
    return aux(m, 0)


def reverse(m: Maillon) -> Liste:
    """
    version 'en place'
    mais confus avec cette nouvelle liste
    """
    def aux(m: Maillon, suivant: Maillon) -> Liste:
        if m.prec is not None:
            temp = m.prec
            m.prec = suivant
            return aux(temp, m)
        m.prec = suivant
        return m
    l = Liste()
    l.premier = aux(m, None)
    return l


def reverse2(m: Maillon) -> Liste:
    """
    version 'copie'
    """
    def aux(m: Maillon, acc: Maillon) -> Maillon:
        if m is None:
            return acc
        else:
            nv = Maillon(m.val)
            nv.prec = acc
            return aux(m.prec, nv)

    l = Liste()
    l.premier = aux(m, l.premier)
    return l


def compress(m: Maillon) -> Liste:
    def aux(m: Maillon, acc: Maillon) -> Maillon:
        if m.prec is not None:
            if m.val == m.prec.val:
                return aux(m.prec, acc)
            else:
                nv = Maillon(m.val)
                nv.prec = acc
                return aux(m.prec, nv)
        else:
            # met le dernier (forcément)
            nv = Maillon(m.val)
            nv.prec = acc
            return nv

    l = Liste()
    l.premier = aux(m, l.premier)
    return l


l = Liste()
l.initialisation(5)
print(l)
print(f"last {last(l.premier)}")
print(f"two last {two_last(l.premier)}")
print(f"k-ieme {k_ieme(l.premier,2)}")
print(f"k-ieme {k_ieme(l.premier,7)}")
print(f"longueur {longueur(l.premier)}")
#print(f"reverse {reverse(l.premier)}")
print(f"reverse2 {reverse2(l.premier)}")
print(l)

l2 = Liste()
l2.add_elt(0)
l2.add_elt(1)
l2.add_elt(1)
l2.add_elt(1)
l2.add_elt(3)
l2.add_elt(4)
l2.add_elt(4)
l2.add_elt(7)
l2.add_elt(7)
l2.add_elt(7)
l2.add_elt(8)
print(l2)
print(f"compress {compress(l2.premier)}")
