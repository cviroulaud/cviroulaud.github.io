#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 12 Mars 2022 08:43
"""
import csv

f = open("geocube.csv", "w")
writer = csv.DictWriter(f, ["Jour", "Heure", "Temperature"])
writer.writeheader()
writer.writerow(
    {"Jour": "2021-12-03", "Heure": "23:09:43", "Temperature": 9.1})
writer.writerow(
    {"Jour": "2021-12-03", "Heure": "23:29:43", "Temperature": 9.4})

f.close()
