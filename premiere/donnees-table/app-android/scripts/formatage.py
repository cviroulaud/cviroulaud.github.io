#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/15 21:21:03
"""

import csv

entree = open("googleplaystore-brut.csv")
data_reader = csv.DictReader(entree)
sortie1 = open("googleplaystore.csv", "w")
sortie2 = open("specifications-app.csv", "w")

attributs1 = ["Name", "Category", "Rating", "Reviews", "Installs"]
attributs2 = ["Name", "Size", "Content Rating",
              "Last Updated", "Current Ver", "Android Ver"]
writer1 = csv.DictWriter(sortie1, attributs1)
writer2 = csv.DictWriter(sortie2, attributs2)
writer1.writeheader()
writer2.writeheader()

table1, table2 = [], []
for app in data_reader:
    dico1, dico2 = {}, {}
    for nom, val in app.items():
        if nom == "Installs":
            # reformatage du nb en entier
            val = val.replace(",", "")
            val = val.replace("+", "")
        if nom == "App":
            #renommer App en Name et le placer dans le second dico (clé primaire)
            nom = "Name"
            dico2[nom] = val
        if nom in attributs1:
            dico1[nom] = val
        elif nom in attributs2:
            dico2[nom] = val
    table1.append(dico1)
    table2.append(dico2)

writer1.writerows(table1)
writer2.writerows(table2)
sortie1.close()
sortie2.close()
entree.close()
