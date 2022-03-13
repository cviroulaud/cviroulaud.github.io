#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Christophe Viroulaud
@Time:   Samedi 12 Mars 2022 00:03

EN TEST

"""
from biblio_graphe import Graphe
import pygame
from pygame.locals import *

TAILLE = 5
DIM = 50
pygame.init()
WHITE = pygame.Color(255, 255, 255)
DELTA = ((-1, 0), (0, -1), (1, 0), (0, 1))
fenetre = pygame.display.set_mode((TAILLE*DIM, TAILLE*DIM))


def tracer_ligne(dep: tuple, arr: tuple) -> None:
    # vertical
    if dep[0] == arr[0]:
        x1 = dep[0]*DIM+DIM//2
        x2 = arr[0]*DIM+DIM//2
        y1 = dep[1]*DIM-DIM//2
        y2 = arr[1]*DIM+DIM//2
    else:  # horizontal
        x1 = dep[0]*DIM+DIM//2
        x2 = arr[0]*DIM-DIM//2
        y1 = dep[1]*DIM+DIM//2
        y2 = arr[1]*DIM+DIM//2
    pygame.draw.line(fenetre, WHITE, (x1, y1), (x2, y2))


labyrinthe = Graphe(False)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            pygame.quit()

    for y in range(TAILLE):
        for x in range(TAILLE):
            for dx, dy in DELTA:
                if x+dx >= 0 and x+dx < TAILLE and y+dy >= 0 and y+dy < TAILLE:
                    labyrinthe.ajouter_arete((x, y), (x+dx, y+dy))

    dfs = labyrinthe.dfs_it((0, 0))
    
    for y in range(TAILLE):
        for x in range(TAILLE):
            if x+dx >= 0 and x+dx < TAILLE and y+dy >= 0 and y+dy < TAILLE:
                if not labyrinthe.sont_relies((x, y), (x+dx, y+dy)):
                    tracer_ligne((x, y), (x+dx, y+dy))
    
    pygame.display.flip()
