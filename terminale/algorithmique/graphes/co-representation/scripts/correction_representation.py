#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Wed Oct 28 11:17:17 2020

@auteur: Christophe Viroulaud
"""

from mod_verification import verifier

matrice_co =  [[0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0],
               [1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0],
               [0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
               [1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
               [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
               [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
               [0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
               [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
               [0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
               [0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1],
               [1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1],
               [0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
               [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0],
               [0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0]]

dico_co = {
    7:{17,19,45},
    10:{18,21,43},
    12:{26,32},
    14:{25,30,32,34,49},
    17:{7,30,34,45},
    18:{10,19,34},
    19:{7,18,43,45},
    21:{10,43},
    25:{14,45,49,75},
    26:{12,71},
    30:{14,17,34,49},
    32:{12,14,49},
    34:{14,17,18,30},
    43:{10,19,21,45,75},
    45:{7,17,19,25,43,75},
    49:{14,25,30,32,65},
    65:{49,70,71,75},
    70:{65,71,75},
    71:{26,65,70},
    75:{25,43,45,65,70}}

verifier(matrice_co)
verifier(dico_co)