#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 12 Mars 2022 09:05
"""

from faker import Faker
from random import randint
import csv

# initialisation du faker en fr
fake = Faker('fr_FR')

f = open("sondage.csv", "w", encoding="utf8")
writer = csv.DictWriter(f, ["nom", "prénom", "age", "profession", "salaire"])
writer.writeheader()

for _ in range(100):
    writer.writerow({"nom": fake.last_name(),
                     "prénom": fake.first_name(),
                     "age": randint(25, 55),
                     "profession": fake.job(),
                     "salaire": randint(1200, 3500)})
f.close()