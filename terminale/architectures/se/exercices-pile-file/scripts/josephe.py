#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mardi 19 Octobre 2021 09:37
"""


from file import File

# Création du cercle
soldats = File()

for i in range(1, 42):
    soldats.enfiler(i)

# Élimination tous les 3
while not(soldats.est_vide()):
    # les non-éliminés reviennent dans la file
    for _ in range(2):
        soldats.enfiler(soldats.defiler())

    # soldat éliminé
    elimine = soldats.defiler()

# dernier éliminé
print(elimine)
