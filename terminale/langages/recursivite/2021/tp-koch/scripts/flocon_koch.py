#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Sun Sep  6 17:58:22 2020

@auteur: Christophe Viroulaud
"""


import turtle

turtle.setheading(0)
turtle.hideturtle()
turtle.speed(0)

def courbe_koch(n,mesure) :
	if n == 0 :
		turtle.forward(mesure)
	else :
		courbe_koch(n-1, mesure//3)
		turtle.left(60)
		courbe_koch(n-1, mesure//3)
		turtle.left(-120)
		courbe_koch(n-1, mesure//3)
		turtle.left(60)
		courbe_koch(n-1, mesure//3)

def flocon(n,mesure) :
	for _ in range(3) :
		courbe_koch(n,mesure)
		turtle.left(-120)

flocon(3,500)

turtle.exitonclick()