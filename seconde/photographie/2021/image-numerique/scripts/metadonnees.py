#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sat Jan  9 20:42:07 2021

@auteur: Christophe Viroulaud
"""


import PIL.Image
img = PIL.Image.open('paysage.jpg')
exif_data = img._getexif()
print(exif_data[34853])