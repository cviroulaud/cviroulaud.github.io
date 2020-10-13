#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Oct 13 08:28:20 2020

@auteur: Christophe Viroulaud
"""


import csv

fichier_histo = open("historique.csv")
historique = list(csv.DictReader(fichier_histo, delimiter=";"))
#with open("historique.csv", delimiter=";") as historique:


fichier_histo.closed()