#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Mon Sep 28 11:01:42 2020

@auteur: Christophe Viroulaud
"""


from PIL import Image

class Image_lib:
    """
    bibliothèque pour travailler sur une image
    """

    def __init__(self, fichier: str)->None:
        self.image = Image.open(fichier)
        self.largeur, self.hauteur = self.image.size
        self.px = self.image.load()

    def rotation_auxiliaire(self, px: object, x: int, y: int, t: int, horaire: bool)->None:
        if t == 1:
            # on ne fait rien: inutile de tourner 1 pixel carré
            return
        else:
            t //= 2
            self.rotation_auxiliaire(self.px, x, y, t, horaire)
            self.rotation_auxiliaire(self.px, x+t, y, t, horaire)
            self.rotation_auxiliaire(self.px, x, y+t, t, horaire)
            self.rotation_auxiliaire(self.px, x+t, y+t, t, horaire)

        for x1 in range(x, x+t):
            for y1 in range(y, y+t):
                if horaire:
                    px[x1,y1+t], px[x1+t,y1+t], px[x1+t,y1  ], px[x1  ,y1] = \
                    px[x1+t,y1+t], px[x1+t  ,y1], px[x1,y1], px[x1,y1+t]
                else:
                    px[x1,y1+t], px[x1+t,y1+t], px[x1+t,y1  ], px[x1  ,y1] = \
                    px[x1,y1  ], px[x1  ,y1+t], px[x1+t,y1+t], px[x1+t,y1]

    def rotation(self, horaire: bool = True)->None:
        """
        tourne l'image de 90°

        Paramètres
        -------
        horaire: booléen; défaut: True
            tourne de 90° dans le sens horaire si True,
            dans le sens anti-horaire sinon
        """
        self.rotation_auxiliaire(self.px, 0, 0, self.largeur, horaire)

    def montrer(self):
        """
        affiche l'image
        """
        self.image.show()

    def sauvegarder(self, nom: str)->None:
        """
        sauvegarde l'image

        Paramètres
        ----------
        nom : str
            nom du fichier de sauvegarde
        """
        self.image.save(nom)

    def filtrer(self, f: str, nom: str)->None:
        """
        crée une image filtrée

        Paramètres
        ----------
        f : str
            filtre à appliquer: r, g ou b
        nom: str
            nom du fichier de sauvegarde
        """
        image_filtree = Image.new("RGB", (self.largeur, self.hauteur))

        for ligne in range(self.hauteur):
            for colonne in range(self.largeur):
                (r,g,b,a) = self.image.getpixel((colonne,ligne))
                if f == "r":
                    image_filtree.putpixel((colonne, ligne),(r,0,0))
                elif f == "g":
                    image_filtree.putpixel((colonne, ligne),(0,g,0))
                else:
                    image_filtree.putpixel((colonne, ligne),(0,0,b))

        image_filtree.show()

"""
Programme principal
"""
im = Image_lib("../ressources/angry.png")
im.montrer()
im.rotation()
im.montrer()
im.rotation(False)
im.montrer()
im.sauvegarder("test.png")

im.filtrer("r","filtre_rouge.png")