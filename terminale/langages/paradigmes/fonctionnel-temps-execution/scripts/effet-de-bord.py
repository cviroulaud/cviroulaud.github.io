#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Sep  8 09:49:06 2020

@auteur: Christophe Viroulaud
"""



notes=[7,12,8,5,19,10,7,6,1,15,13,8]
print(notes)

def majoration(bonus: int):
    for i in range(len(notes)):
        if notes[i]<=8:
            notes[i]+=bonus

majoration(2)
print(notes)
majoration(3)
print(notes)
