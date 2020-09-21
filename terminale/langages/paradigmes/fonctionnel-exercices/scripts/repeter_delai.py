#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Sep 20 20:44:39 2020

@auteur: Christophe Viroulaud
"""

from time import sleep
import turtle as t

#Question 1
def repeter_delai(f, n: int, t: int)->None:
    for i in range(n):
        f(i)
        sleep(t)

#Question 2
def dessine(n: int)->None:
    t.forward(n*50)
    t.left(90)

#Question 3
repeter_delai(dessine, 10, 1)
t.bye()