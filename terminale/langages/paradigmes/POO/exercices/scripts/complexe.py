#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep  9 13:51:00 2020

@auteur: Christophe Viroulaud
"""


class Complexe:

    def __init__(self, re: float, im: float):
        self.a = re
        self.b = im

    def addition(self, z) -> tuple:
        return (self.a + z.a, self.b + z.b)

    def soustraction(self, z) -> tuple:
        return (self.a - z.a, self.b - z.b)

    def afficher(self) -> str:
        return f"{self.a} + i*{self.b}"


z = Complexe(3, 5)
print(z.afficher())
print(z.addition(Complexe(8, 2)))
