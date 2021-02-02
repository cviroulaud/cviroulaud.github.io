#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Feb  1 10:04:59 2021

@auteur: Christophe Viroulaud
"""


# Pour respecter la numérotation de Sosa-Stradonitz la première cellule est laissée vide
macron = ["", "Emmanuel Macron", "Jean-Michel Macron", "Françoise Noguès",
          "André-Henri Macron", "Jacqueline Robertson", "Jean Noguès",
          "Germaine Arribet", "Henri Eugène Macron", "Marie Adèle Bosseur",
          "Georges William Robertson", "Suzanne Leblond", "Fabien Noguès",
          "Esther Mas", "Ernest Arribet", "Marie Madeleine Millet"]

def get_parents(tab: list, id_enfant: int)->tuple:
    # vérifie si on est encore dans le tableau
    assert 2*id_enfant < len(tab), "Nous ne sommes pas remontés aussi loin."
    return(tab[2*id_enfant], tab[2*id_enfant+1])

def ascendant_homme(tab: list, hommes: list)->list:
    p = []
    p.append(1)
    while len(p) > 0:
        en_cours = p.pop()
        if en_cours < len(tab):
            # enregistre ascendant hommes
            if en_cours%2 == 0 and en_cours > 1:
                hommes.append(tab[en_cours])

            p.append(2*en_cours+1)
            p.append(2*en_cours)
    return hommes

def ascendant_homme_rec(tab: list, hommes: list, en_cours: int = 1)->list:
    if en_cours < len(tab):
        # enregistre ascendant hommes
        if en_cours%2 == 0 and en_cours > 1:
            hommes.append(tab[en_cours])

        ascendant_homme_rec(tab, hommes, 2*en_cours)
        ascendant_homme_rec(tab, hommes, 2*en_cours+1)
    return hommes


print(get_parents(macron, 1))

print(ascendant_homme(macron, []))
print(ascendant_homme_rec(macron, []))

print(get_parents(macron, 15))