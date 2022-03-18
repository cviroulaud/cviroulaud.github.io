#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/21 17:48:21
"""

import matplotlib.pyplot as plt

frequence = [8.15, 0.97, 3.15, 3.73, 17.39, 1.12, 0.97,
             0.85, 7.31, 0.45, 0.02, 5.69, 2.87, 7.12,
             5.28, 2.8, 1.21, 6.64, 8.14, 7.22, 6.38,
             1.64, 0.03, 0.41, 0.28, 0.15]

alphabet = [chr(i) for i in range(65,91)]

plt.bar(alphabet,frequence)
plt.show()