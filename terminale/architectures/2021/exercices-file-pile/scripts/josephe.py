#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Oct 16 13:46:54 2020

@auteur: Christophe Viroulaud
"""


from mod_file import File

#Création du cercle
soldats = File()

for i in range(1,42):
    soldats.enfiler(i)

#Élimination tous les 3
while not(soldats.est_vide()):
	for _ in range(2):
		soldats.enfiler(soldats.defiler())

    #soldat éliminé
	elimine = soldats.defiler()

#dernier éliminé
print(elimine)