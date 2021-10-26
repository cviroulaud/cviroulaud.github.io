#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 25 Octobre 2021 00:26
"""
vehicule1 = {"marque": "Renault", 
            "modele": "Twingo", 
            "kilometrage": 23410, 
            "immatriculation": "AA-123-AA", 
            "premiere_imat": "2010-10", 
            "date_vidange": "2020-01"}

vehicule1["couleur"] = "rouge"
print(vehicule1["puissance"])

print(vehicule1)
print(len(vehicule1))

for cle in vehicule1.keys():
    print(cle)

for val in vehicule1.values():
    print(val)

for cle, val in vehicule1.items():
    print(cle, " -> ", val)