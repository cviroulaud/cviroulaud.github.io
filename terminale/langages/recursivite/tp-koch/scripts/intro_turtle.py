#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Sep  6 16:39:50 2020

@auteur: Christophe Viroulaud
"""


import turtle
from random import randint

def hex_couleur():
    couleur="#"
    for _ in range(3):
        c=hex(randint(0,255))[2:]
        if len(c)<2:
            couleur+='0'+c
        else:
            couleur+=c
    return couleur

turtle.speed(0)
turtle.hideturtle()

for i in range(10):
    couleur=hex_couleur()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.right(36)

turtle.exitonclick()