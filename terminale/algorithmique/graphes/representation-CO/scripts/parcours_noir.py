#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Vendredi 28 Janvier 2022 23:43
"""
import json

f = open("parcours_noir.json")
donnees = json.load(f)  # tableau de dictionnaires
dico_adj = {}
for info in donnees:
    sommet = info["sommet"]
    adjacents = info["adjacents"]
    dico_adj[sommet] = adjacents
f.close()
print(dico_adj)
