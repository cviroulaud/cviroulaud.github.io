#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep  9 13:51:00 2020

@auteur: Christophe Viroulaud
"""


class Complexe:

    def __init__(self, re: float, im: float):
        self.reel = re
        self.imaginaire = im

    def get_reel(self) -> float:
        return self.reel

    def get_imaginaire(self) -> float:
        return self.imaginaire

    def addition(self, c):
        # nous effectuerons du typing uniquement pour types de base
        return (self.reel + c.reel, self.imaginaire + c.imaginaire)

    def afficher(self) -> str:
        return f"{self.reel} + i*{self.imaginaire}"

z = Complexe(3, 5)
print(z.afficher())
print(z.addition(Complexe(8, 2)))