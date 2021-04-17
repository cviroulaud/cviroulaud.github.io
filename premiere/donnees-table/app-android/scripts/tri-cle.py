#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/16 21:47:36
"""

import csv

f = open("notes.csv")
data = csv.DictReader(f)
eleves = []
for e in data:
    dico = {"nom": e["nom"], "prenom": e["prenom"],
            "moyennes": float(e["moyennes"])}
    eleves.append(dico)
f.close()


def parametres_tri(eleve: dict) -> float:
    """
    renvoie le paramètre utilisé pour le tri
    """
    return eleve["moyennes"]

eleves.sort(key=parametres_tri)
print(eleves)
