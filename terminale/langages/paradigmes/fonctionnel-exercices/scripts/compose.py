#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Sep 21 09:30:08 2020

@auteur: Christophe Viroulaud
"""


def h(f,g):
    return lambda x: f(g(x))

f = lambda x: x**2
g = lambda x: 2*x+3

print(h(f,g)(5))