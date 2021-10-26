#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Oct 24 21:45:00 2020

@auteur: Christophe Viroulaud
"""

"""
Anomalie de la température moyenne annuelle de l'air, en surface, par rapport
à la normale de référence : température moyenne en France (l'indicateur est
constitué de la moyenne des températures de 30 stations météorologiques.
Le zéro correspond à la moyenne de l'indicateur sur la période 1961-1990,
soit 11,8 °C).
"""
import matplotlib.pyplot as plt

temperatures = [0.3, -0.7, -0.6, -0.3, 0.1, -0.6, 0.0, -0.4, -0.4, -1.0,
                -0.4, 0.5, -0.4, 0.1, -0.3, -0.4, -0.2, -1.2, -0.2, -0.7,
                0.0, 0.6, -0.7, -0.1, -0.4, -0.6, 0.3, -0.1, 0.5, -0.2,
                0.4, -0.6, -0.3, -0.2, 0.4, -0.1, 0.0, 0.5, -0.1, -0.3,
                -0.9, -0.9, -0.4, 0.7, -0.4, 0.6, -0.3, 0.8, 0.3, 0.8,
                0.2, -0.1, 0.1, 0.1, -0.5, 0.0, -1.2, 0.0, 0.0, 0.8,
                0.0, 0.8, -0.8, -1.1, -0.1, -0.5, 0.2, 0.1, -0.2, -0.2,
                -0.1, -0.2, -0.5, -0.2, 0.1, 0.0, 0.3, 0.1, -0.4, -0.2,
                -0.6, 0.1, 0.8, 0.6, -0.2, -0.5, -0.2, -0.1, 0.7, 1.2,
                1.2, 0.2, 0.5, 0.2, 1.5, 1.0, 0.1, 1.3, 0.7, 1.2,
                1.3, 1.0, 1.3, 1.7, 0.8, 0.8, 1.4, 1.1, 0.7, 1.2,
                0.1, 1.8, 1.0, 0.6, 1.9, 1.7, 1.2, 1.6]

temperatures.append(2.1)
temperatures.append(1.8)

plt.bar(range(1900, 2020), temperatures)
plt.title("Anomalie des températures 1900-2019")
plt.show()
