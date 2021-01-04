#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Sep  8 09:49:06 2020

@auteur: Christophe Viroulaud
"""


def simulation_bonification(limite):
    for i in range(len(notes)):
        if notes[i] <= limite:
            notes[i] += 2
    return notes

notes=[7,12,8,5,19,10,7,6,1,15,13,8]
print(notes)
print(simulation_bonification(6))
print(simulation_bonification(8))

