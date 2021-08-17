#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Oct 17 20:54:33 2020

@auteur: Christophe Viroulaud
"""


import turtle as t

for i in range(10):
    """
    i est pair (le reste de la division par 2 est nul)
    """
    if i%2 == 0:
        t.color("green", "green")
    else:
        t.color("red", "red")

    t.begin_fill()
    # on trace le carré
    for j in range(4):
        t.forward(100)
        t.left(90)

    t.end_fill()

    # on tourne de 36° pour faire le tour complet
    t.left(36)

t.done()