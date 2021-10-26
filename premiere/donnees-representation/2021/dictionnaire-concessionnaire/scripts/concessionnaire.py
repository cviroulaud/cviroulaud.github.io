#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Feb 17 23:14:47 2021

@auteur: Christophe Viroulaud
"""


vehicule1 = {"marque": "Renault",
		"modele": "Twingo",
		"kilometrages": 23410,
		"immatriculation": "AA-123-AA",
		"premiere_imat": "2010-10",
		"date_vidange": "2020-01"}

for cle in vehicule1.keys():
    print(cle)

for val in vehicule1.values():
    print(val)

for cle, val in vehicule1.items():
    print(cle, val)