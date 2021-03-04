#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/03 15:55:38
"""

def fibo_top_down(n: int, track: list)->int:
    """
    calcule le terme de rang n
    de la suite de Fibonacci
    """
    if track[n] > 0:
        return track[n]
    if n == 0:
        track[0] = 0 
        return track[0]
    elif n == 1:
        track[1] = 1
        return track[1]
    else:
        track[n] = fibo_top_down(n-1, track) + fibo_top_down(n-2, track)
        return track[n]

n = 20
track = [-1 for _ in range(n+1)]
fibo_top_down(n, track)

def fibo_bottom_up(n: int)->int:
    track = [0 for _ in range(n+1)]
    track[1] = 1
    for i in range(2, n+1):
        track[i] = track[i-1] + track[i-2]
    return track[n]

print(fibo_bottom_up(20))

def fibo_bottom_up2(n: int)->int:
    track0 = 0
    track1 = 1
    for i in range(2, n+1):
        track0, track1 = track1, track0 + track1
    return track1

print(fibo_bottom_up2(20))