#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Jeudi 21 Octobre 2021 22:50
"""
from time import sleep

INTERMEDIAIRE = 0


def calcul():
    global INTERMEDIAIRE
    print("section non critique 1")


    for c in range(400):
        temp = INTERMEDIAIRE

        # simule un traitement nécessitant des calculs
        sleep(0.000000001)

        INTERMEDIAIRE = temp + 1
        
    print("section non critique 2")


calcul()
print(INTERMEDIAIRE)
