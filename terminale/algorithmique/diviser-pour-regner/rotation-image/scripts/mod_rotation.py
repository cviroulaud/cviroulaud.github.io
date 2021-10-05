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

    def __init__(self, fichier: str) -> None:
        self.image = Image.open(fichier)
        self.largeur, self.hauteur = self.image.size
        self.px = self.image.load()

    def tourner_antihoraire(self, x: int, y: int, t: int) -> None:
        for l in range(y, y+t):
            for c in range(x, x+t):
                self.px[l, c+t], self.px[l+t, c+t], \
                    self.px[l+t, c], self.px[l, c] = \
                    self.px[l, c], self.px[l, c + t], \
                    self.px[l+t, c+t], self.px[l+t, c]

    def tourner_horaire(self, x: int, y: int, t: int) -> None:
        for l in range(y, y+t):
            for c in range(x, x+t):
                self.px[l, c+t], self.px[l+t, c+t], \
                    self.px[l+t, c], self.px[l, c] = \
                    self.px[l+t, c+t], self.px[l+t, c], \
                    self.px[l, c], self.px[l, c+t]

    def rotation(self, x: int, y: int, t: int, horaire: bool) -> None:
        if t > 1:
            t //= 2
            self.rotation(x, y, t, horaire)
            self.rotation(x+t, y, t, horaire)
            self.rotation(x, y+t, t, horaire)
            self.rotation(x+t, y+t, t, horaire)

            if horaire:
                self.tourner_horaire(x, y, t)
            else:
                self.tourner_antihoraire(x, y, t)

    def fait_tourner(self, horaire: bool = True) -> None:
        """
        tourne l'image de 90°

        Paramètres
        -------
        horaire: booléen; défaut: True
            tourne de 90° dans le sens horaire si True,
            dans le sens anti-horaire sinon
        """
        self.rotation(0, 0, self.largeur, horaire)

    def montrer(self):
        """
        affiche l'image
        """
        self.image.show()

    def sauvegarder(self, nom: str) -> None:
        """
        sauvegarde l'image

        Paramètres
        ----------
        nom : str
            nom du fichier de sauvegarde
        """
        self.image.save(nom)

    def filtrer(self, f: str, nom: str) -> None:
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
                (r, g, b, a) = self.image.getpixel((colonne, ligne))
                if f == "r":
                    image_filtree.putpixel((colonne, ligne), (r, 0, 0))
                elif f == "g":
                    image_filtree.putpixel((colonne, ligne), (0, g, 0))
                else:
                    image_filtree.putpixel((colonne, ligne), (0, 0, b))

        image_filtree.show()


if __name__ == "__main__":
    im = Image_lib("../ressources/angry.png")
    im.montrer()
    im.fait_tourner()
    im.montrer()
    im.fait_tourner(False)
    im.montrer()
    # im.sauvegarder("test.png")

    im.filtrer("r", "filtre_rouge.png")
