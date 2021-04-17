#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/16 15:41:42
"""

import csv
fichier = open("notes.csv")

lecteur1 = csv.reader(fichier)
for ligne in lecteur1:
    print(ligne)

fichier.close()

fichier = open("notes.csv")

lecteur2 = csv.DictReader(fichier)
for ligne in lecteur2:
    print(ligne)

fichier.close()