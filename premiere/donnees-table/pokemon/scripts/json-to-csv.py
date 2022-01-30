#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/28 16:14:04
"""

import csv
import json

f = open("pokedex.csv", "w")
attributs = ["num", "name", "type", "height", "img",
             "weight", "egg", "weaknesses", "next_evolution"]
writer = csv.DictWriter(f, attributs)
writer.writeheader()

table = []
with open("pokedex.json") as fjson:
    data = json.load(fjson)["pokemon"]

for pokemon in data:
    dico = {}
    for attr in attributs:
        # on ne prend qu'un type et qu'une faiblesse
        if attr == "type" or attr == "weaknesses":
            dico[attr] = pokemon[attr][0]
        # on modifie la numérotation pour coller avec les widgets
        elif attr == "num":
            dico[attr] = int(pokemon[attr])-1
        # on ne prend que le num de la première évolution
        elif attr == "next_evolution":
            # s'il a une évolution
            if "next_evolution" in pokemon:
                dico[attr] = int(pokemon[attr][0]["num"])-1
            else:
                dico[attr] = -1  # pas d'évolution
        # enlève unité
        elif attr == "height":
            dico[attr] = pokemon[attr][:-2]
        # enlève unité
        elif attr == "weight":
            dico[attr]=pokemon[attr][:-3]
        # modifier l'adresse web par locale
        elif attr == "img":
            dico[attr] = "pokemon/"+pokemon["name"]+".png"
        else:
            dico[attr] = pokemon[attr]
    table.append(dico)

writer.writerows(table)
f.close()
