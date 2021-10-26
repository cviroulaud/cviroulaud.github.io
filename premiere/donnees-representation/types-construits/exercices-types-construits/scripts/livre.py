#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 25 Octobre 2021 15:12
"""

bibliotheque = [
    {"titre": "Il était deux fois",
     "auteur": "Franck Thilliez",
     "editeur": "Poche",
     "prix": 8.70},
    {"titre": "Fahrenheit 451",
     "auteur": "Ray Bradbury",
     "editeur": "Folio",
     "prix": 6.30}
]

for livre in bibliotheque:
    # livre contient un dictionnaire
    print(livre["auteur"])
