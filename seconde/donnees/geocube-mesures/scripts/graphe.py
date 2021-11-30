#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Lundi 29 Novembre 2021 13:10
"""

import matplotlib.pyplot as plt
import csv

fichier = open("temperature.csv")
lecteur = csv.DictReader(fichier)
fichier2 = open("pression.csv")
lecteur2 = csv.DictReader(fichier2)
temp = []
pression=[]
for ligne in lecteur:
    temp.append(float(ligne["GV6_0025"]))
fichier.close()

for ligne in lecteur2:
    pression.append(float(ligne["GV6_0025"]))
fichier2.close()

fig, ax1 = plt.subplots()
ax1.plot(temp,'red')
ax1.set_ylim(20,40)

ax2 = ax1.twinx()
ax2.plot(pression,'blue')

plt.show()