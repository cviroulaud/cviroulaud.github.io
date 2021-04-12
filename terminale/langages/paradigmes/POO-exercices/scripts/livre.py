#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Sep  9 13:51:00 2020

@auteur: Christophe Viroulaud
"""


class Livre:

    def __init__(self, t: str, a: str, p: int):
        self.titre = t
        self.auteur = a
        self.prix = p

    def get_titre(self) -> str:
        return self.titre

    def set_titre(self, t: str) -> None:
        self.titre = t

    def afficher(self) -> str:
        # return "{} est écrit par {}.".format(self.titre, self.auteur)
        return f"{self.titre} est écrit par {self.auteur}."

livre1 = Livre("La guerre des mondes", "Herbert Wells", 7)
print(livre1.afficher())