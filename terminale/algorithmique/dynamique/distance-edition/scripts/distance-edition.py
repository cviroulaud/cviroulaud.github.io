#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 25 Février 2022 11:56

http://www.xavierdupre.fr/blog/2013-12-02_nojs.html
"""

CMP = 0


def distance(mot1: str, mot2: str, i: int, j: int) -> list:
    global CMP
    if i == 0:
        return j
    elif j == 0:
        return i
    else:
        CMP += 1
        d_suppr = distance(mot1, mot2, i-1, j)+1
        d_inser = distance(mot1, mot2, i, j-1)+1
        d_comp = distance(mot1, mot2, i-1, j-1)
        if mot1[i-1] != mot2[j-1]:
            d_comp = d_comp+1
        return min(d_suppr, d_inser, d_comp)


def distance_TD(mot1: str, mot2: str, i: int, j: int, track: list) -> list:
    global CMP
    if track[i][j] >= 0:
        return track[i][j]
    elif i == 0:
        track[i][j] = j
        return j
    elif j == 0:
        track[i][j] = i
        return i
    else:
        CMP += 1
        d_suppr = distance_TD(mot1, mot2, i-1, j, track)+1
        d_inser = distance_TD(mot1, mot2, i, j-1, track)+1
        d_comp = distance_TD(mot1, mot2, i-1, j-1, track)
        if mot1[i-1] != mot2[j-1]:
            d_comp = d_comp+1
        track[i][j] = min(d_suppr, d_inser, d_comp)
        return track[i][j]


m1 = "idstzance"
m2 = "distances"
track = [[-1 for j in range(len(m2))] for i in range(len(m1))]
print(distance(m1, m2, len(m1)-1, len(m2)-1))
print(CMP)
CMP = 0
print(distance_TD(m1, m2, len(m1)-1, len(m2)-1, track))
print(CMP)
