#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 23 Octobre 2021 23:50
"""


def a_gagne(palmares: tuple, equipe: str) -> bool:
    """
    vérifie si l'équipe a déjà gagné
    """
    for i in range(len(palmares)):
        if palmares[i] == equipe:
            return True
    # on a parcouru tout le tuple
    return False


def a_gagne2(palmares: tuple, equipe: str) -> bool:
    """
    vérifie si l'équipe a déjà gagné
    """
    for e in palmares:
        if e == equipe:
            return True
    # on a parcouru tout le tuple
    return False


def nombre_victoires(palmares: tuple, equipe: str) -> int:
    """
    nombre de victoires de l'équipe
    """
    victoires = 0
    for i in range(len(palmares)):
        if palmares[i] == equipe:
            victoires += 1

    return victoires


def nombre_victoires2(palmares: tuple, equipe: str) -> int:
    """
    nombre de victoires de l'équipe
    """
    victoires = 0
    for e in palmares:
        if e == equipe:
            victoires += 1

    return victoires


gagnants = ("Nouvelle-Zélande", "Australie",
            "Afrique du Sud", "Australie",
            "Angleterre", "Afrique du Sud",
            "Nouvelle-Zélande", "Nouvelle-Zélande",
            "Afrique du Sud")

for i in range(3):
    print(gagnants[i])

print(a_gagne(gagnants, "Nouvelle-Zélande"))
print(nombre_victoires(gagnants, "Australie"))
