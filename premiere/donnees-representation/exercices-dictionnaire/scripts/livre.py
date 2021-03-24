#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/03/24 22:08:20
"""

bibliotheque = [
    {"titre": "Il était deux fois", 
     "auteur": "Franck Thilliez",
     "editeur": "Poche",
     "prix": 8.70},
    {"titre": "Fahrenheit 451", 
     "auteur": "Ray Bradbury",
     "editeur": "Folio",
     "prix": 6.30},
    {"titre": "Le guide du voyageur galactique", 
     "auteur": "Douglas Adams",
     "editeur": "Folio",
     "prix": 8.10},
    {"titre": "Il était deux fois", 
     "auteur": "Franck Thilliez",
     "editeur": "Poche",
     "prix": 8.70}
]

for livre in bibliotheque:
    print(livre["auteur"])