#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 11:33:15 2020

@auteur: Christophe Viroulaud
"""


class Pile:
    def __init__(self):
        self.donnees = []

    def estVide(self):
        return self.donnees == []

    def empiler(self, e):
        self.donnees.append(e)

    def depiler(self):
        if not self.estVide():
            return self.donnees.pop()

    def __str__(self):
        affiche =""
        for x in self.donnees:
            affiche = str(x)+"\n"+affiche
        return affiche

class File:
    def __init__(self):
        self.donnees = []

    def estVide(self):
        return self.donnees == []

    def enfiler(self, e):
        self.donnees.append(e)

    def defiler(self):
        if not self.donnees == []:
            return self.donnees.pop(0)

    def __str__(self):
        affiche = ""
        for x in self.donnees:
            affiche += str(x) + " "
        return affiche