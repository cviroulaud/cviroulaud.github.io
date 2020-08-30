#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Aug 19 15:04:24 2020

@auteur: Christophe Viroulaud
"""


from mod_banque import Banque

BdP=Banque("Banque des Périgourdins",1.01)
print(BdP.nom)

#création des clients
BdP.cree_client("Jay")
BdP.cree_client("Laure")
BdP.cree_client("Bertran")

#crédite comptes Jay
jay=BdP.trouve_client("Jay")
comptes_jay=jay.get_comptes()
for compte in comptes_jay.values():
    if compte.est_remunere:
        compte.credite(200)
    else:
        compte.credite(1000)

#vérifie comptes Jay
for compte in comptes_jay.values():
    if compte.est_remunere:
        print("Compte rémunéré:",compte.get_credit())
    else:
        print("Compte courant:",compte.get_credit())

#rémunère comptes
BdP.remunere()

#vérifie comptes Jay
for compte in comptes_jay.values():
    if compte.est_remunere:
        print("Compte rémunéré:",compte.get_credit())
    else:
        print("Compte courant:",compte.get_credit())

