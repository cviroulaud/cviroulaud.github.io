#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/07/25 15:13:36
"""


class Fraction:
    def __init__(self):
        self.numerateur: int = 1
        self.denominateur: int = 1

    def get_numerateur(self) -> int:
        return self.numerateur

    def get_denominateur(self) -> int:
        return self.denominateur

    def set_numerateur(self, n: int) -> None:
        self.numerateur = n

    def set_denominateur(self, d: int) -> None:
        assert d != 0, "Le dénominateur ne peut pas être nul."
        self.denominateur = d

    def __eq__(self, f):
        return self.numerateur * f.denominateur == self.denominateur * f.numerateur

    def __lt__(self, f):
        return self.numerateur * f.denominateur < self.denominateur * f.numerateur

    def __add__(self, f):
        res = Fraction()
        res.set_numerateur(self.numerateur * f.denominateur +
                           f.numerateur * self.denominateur)
        res.set_denominateur(self.denominateur * f.denominateur)
        return res

    def __mul__(self, f):
        res = Fraction()
        res.set_numerateur(self.numerateur * f.numerateur)
        res.set_denominateur(self.denominateur * f.denominateur)
        return res

    def __str__(self):
        return "{}/{}".format(self.numerateur, self.denominateur)


if __name__ == "__main__":
    f = Fraction()
    f.set_numerateur(2)
    f.set_denominateur(3)
    print(f)

    f1 = Fraction()
    f1.set_numerateur(8)
    f1.set_denominateur(12)
    print(f == f1)

    f2 = Fraction()
    f2.set_numerateur(12)
    f2.set_denominateur(7)
    print(f + f2)

    f.set_denominateur(0)
