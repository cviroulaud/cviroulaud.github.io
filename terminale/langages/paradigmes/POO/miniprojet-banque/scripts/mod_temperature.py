#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date de création Fri Aug 21 08:47:54 2020

@auteur: Christophe Viroulaud
"""


class Temperature:
    """
    crée une température en degré Celsius; la température est initialisée à 0°C.

    Paramètres:
            -----
            celsius: float
            température en degré Celsius
    """

    def __init__(self) -> None:
        self.celsius = 0

    def definir_temp(self, c: float) -> None:
        """
        Définit la température en degré Celsius.

        Paramètres
        ----------
        c : float
            degré Celsius.

        Renvoie
        -------
        None
        """
        self.celsius = c

    def affiche_temp(self) -> str:
        """
        Affiche la température en degré Celsius

        Renvoie
        -------
        str

        """
        return "La température est {}°C".format(self.celsius)

    def convertir(self) -> float:
        """
        Convertit la température en Kelvin.

        Returns
        -------
        float
            Kelvin avec une précision au centième.

        """
        return round(self.celsius+273.15, 2)

    def convertir2(self) -> float:
        """
        Convertit la température en degré Fahrenheit.

        Returns
        -------
        float
            degré Fahrenheit avec une précision au centième.

        """
        return round(self.celsius*9/5+32, 2)


if __name__ == "__main__":
    t = Temperature()
    t.definir_temp(11.9)
    print(t.affiche_temp())
    print(t.convertir())
    print(t.convertir2())
    help(Temperature)
