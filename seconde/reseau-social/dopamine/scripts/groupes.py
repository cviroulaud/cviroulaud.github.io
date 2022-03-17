#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Mercredi 16 Mars 2022 11:45
"""
import csv
from random import shuffle
from math import ceil

snt = ["2E", "2I", "2J"]
for s in snt:
    f = open("classe-"+s+".csv", "r", encoding="utf8")
    sortie = open("groupes"+s+".csv", "w", encoding="utf8")

    classe = (list(csv.reader(f)))
    shuffle(classe)

    w = csv.writer(sortie, delimiter=";")

    groupes = []
    i = 0
    g = []
    for e in classe:
        if i % 3 == 0:
            groupes.append(g)
            g = []

        g += e
        i += 1

    if len(g) > 0:
        groupes.append(g)

    w.writerows(groupes)
    f.close()
    sortie.close()
