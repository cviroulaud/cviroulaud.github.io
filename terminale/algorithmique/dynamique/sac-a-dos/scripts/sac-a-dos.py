#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Dimanche 12 Septembre 2021 16:02
"""


class Objet:
    def __init__(self, v: int, w: int):
        self.valeur = v
        self.poids = w


objets = [Objet(0, 0), Objet(1, 2), Objet(2, 5),
          Objet(3, 7), Objet(7, 12), Objet(10, 9)]
poids_max = 15

solutions = [[0 for _ in range(poids_max+1)]for _ in range(len(objets))]

for w in range(1, poids_max+1):
    for i in range(1,len(objets)):
        # si le poids de l'objet <= contenance
        if objets[i].poids <= w:
            # - on ne prend pas l'objet -> prend sol optimale précédente
            # - on prend l'objet -> sol optimale ligne avant + valeur de l'objet
            solutions[i][w] = max(
                solutions[i-1][w], solutions[i-1][w-objets[i].poids]+objets[i].valeur)
        else:  # on ne prend pas l'objet (trop lourd)
            solutions[i][w] = solutions[i-1][w]

# affichage solution
print(solutions)
val = solutions[len(objets)-1][poids_max]
poids = poids_max
objet = len(objets)-1
while val > 0:
    if solutions[objet][poids] > solutions[objet-1][poids]:
        print(objets[objet].valeur)
        val -= objets[objet].valeur
        poids -= objets[objet].poids
    objet -= 1
