#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   2021/04/29 18:01:06
"""

import requests
import csv

f = open("pokedex.csv")
reader = csv.DictReader(f)

for pok in reader:
    r = requests.get(pok["img"], allow_redirects=True)
    open(pok["name"]+".png", 'wb').write(r.content)

f.close()