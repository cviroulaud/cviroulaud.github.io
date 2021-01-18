#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Jan 18 13:01:42 2021

@auteur: Christophe Viroulaud
"""


import json
f = open("recette-fondant.json")
recette = json.load(f)
f.close()
print(recette["recette"])