#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Jan  1 16:21:51 2021

@auteur: Christophe Viroulaud
"""


import turtle as t

def triangle(c: int)->None:
    t.begin_fill()
    for _ in range(3):
        t.forward(c)
        t.left(120)
    t.end_fill()

t.up()
for _ in range(3):
    t.left(90)
    t.forward(50)
    t.right(90)
    triangle(100)
t.done()
