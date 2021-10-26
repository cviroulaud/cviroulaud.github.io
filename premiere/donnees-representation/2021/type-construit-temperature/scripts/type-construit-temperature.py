#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Oct 24 21:45:00 2020

@auteur: Christophe Viroulaud
"""


import matplotlib.pyplot as plt

temperatures = (24.5, 25.2, 29.2, 33.0, 27.8, 23.2, 24.2, 29.0, 31.9, 31.0,
                30.6, 31.1, 33.4, 35.4, 32.0, 33.1, 34.3, 30.0, 28.7, 23.0,
                25.1, 22.2, 24.7, 20.5, 16.9, 13.9, 12.4, 18.9, 19.8, 14.9)

"""
plt.plot(range(1,31),temperatures)
plt.title("Septembre 2020")
plt.show()
"""
plt.bar(range(1,31),temperatures)
plt.show()