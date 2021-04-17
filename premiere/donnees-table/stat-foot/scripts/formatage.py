#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/15 18:44:51
"""

import csv

sortie = open("joueurs.csv", "w")
writer = csv.DictWriter(sortie, ["joueur", "nationalité", "équipe", "âge", "naissance",
                        "matchs joués", "minutes jouées", "buts", "passes décisives", "carton jaune", "carton rouge"])
writer.writeheader()
with open("joueur-brut.csv") as f:
    data = csv.DictReader(f)
    table = []
    for j in data:
        nom, nom1 = j["joueur"].split("\\")
        nat, nat1 = j["nationalité"].split()
        j["joueur"] = nom
        j["nationalité"] = nat1
        table.append(j)
    writer.writerows(table)
    sortie.close()
