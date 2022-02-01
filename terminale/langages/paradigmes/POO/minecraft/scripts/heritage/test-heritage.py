#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 31 Janvier 2022 08:39
"""


class Animal:
    def __init__(self, n: str):
        self._nom = n
        self.manger = ""

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, n):
        self._nom = n

    def mange(self, m):
        self.manger = m


class Carnivore(Animal):
    def __init__(self, n):
        super().__init__(n)
        self.croc = False

    def mange(self, m):
        super().mange(m)
        self.croc = True


a = Animal("chien")
print(a.nom)
a.nom = "chat"
print(a.nom)
c = Carnivore("dino")
print(type(c))
c.mange("viande")
print(c.manger)
