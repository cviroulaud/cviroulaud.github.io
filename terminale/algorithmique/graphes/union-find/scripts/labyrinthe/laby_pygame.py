#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Date de création Fri Nov 13 22:21:39 2020

@auteur: Christophe Viroulaud
"""

import pygame
import sys

from constantes import *
from union_find import set_arbre_couvrant

pygame.init()

# Création de la fenêtre Pygame
fenetre = pygame.display.set_mode((largeur*taille, hauteur*taille))
icone = pygame.image.load(img_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption(titre)

mur_h = pygame.image.load(img_mur)
mur_h = pygame.transform.scale(mur_h, (taille, taille//10))
mur_v = pygame.image.load(img_mur)
mur_v = pygame.transform.rotate(mur_v, 90)
mur_v = pygame.transform.scale(mur_v, (taille//10, taille))
        
        
labyrinthe = set_arbre_couvrant()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # affichage
    fenetre.fill((255, 255, 255))
    # murs horizontaux
    for y in range(hauteur):
        for x in range(largeur-1):
            if ((x,y),(x+1,y)) not in labyrinthe and ((x+1,y),(x,y)) not in labyrinthe:
                fenetre.blit(mur_v, ((x+1)*taille,y*taille))
    
    for x in range(largeur):
        for y in range(hauteur-1):
            if ((x,y+1),(x,y)) not in labyrinthe and ((x,y),(x,y+1)) not in labyrinthe:
                fenetre.blit(mur_h, (x*taille,(y+1)*taille))


    pygame.display.flip()
