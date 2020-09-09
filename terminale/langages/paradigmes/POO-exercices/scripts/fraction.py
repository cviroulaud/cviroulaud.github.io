#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Aug 21 10:10:53 2020

@auteur: Christophe Viroulaud
"""


class Fraction:

    def __init__(self, num: int, den: int):
        if den < 0:
            raise ValueError(f"{den} doit être strictement positif.")
        self.numerateur = num
        self.denominateur = den

    def __eq__(self, f):
        return self.numerateur * f.denominateur == self.denominateur * f.numerateur

    def __lt__(self, f):
        return self.numerateur * f.denominateur < self.denominateur * f.numerateur

    def __add__(self, f):
        return Fraction(self.numerateur * f.denominateur + f.numerateur * self.denominateur,
                        self.denominateur * f.denominateur)

    def __mul__(self, f):
        return Fraction(self.numerateur * f.numerateur, self.denominateur * f.denominateur)

    def __str__(self):
        if self.denominateur == 1:
            return str(self.numerateur)
        else:
            return f"{self.numerateur}/{self.denominateur}"

f = Fraction(12,7)
print(f)
print(f == Fraction(24, 14))
print(f + Fraction(2, 3))