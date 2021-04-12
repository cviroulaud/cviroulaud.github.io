#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Tue Nov 24 22:44:14 2020

@auteur: Christophe Viroulaud
"""


import json

with open("fr-esr-parcoursup.json", "r") as fichier:
    data = json.load(fichier)
    print(data[0]["fields"]["g_ea_lib_vx"])