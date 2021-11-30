class Maillon:
    def __init__(self, v, s):
        self.valeur = v
        self.suivant = s


class File:
    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        # pas de difficulté majeure
        nouveau_maillon = Maillon(element, self.dernier_file)
        self.dernier_file = nouveau_maillon

    def est_vide(self):
        return self.dernier_file == None

    def affiche(self):
        # attention: l'affichage ressemble à une pile
        maillon = self.dernier_file
        while maillon != None:
            # on parcourt toute la liste (un print dans une fonction, beurk!!)
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self):
        if not self.est_vide():
            # il n'y a qu'un maillon
            if self.dernier_file.suivant == None:
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            # on parcourt toute la liste pour trouver le premier arrivé
            maillon = self.dernier_file
            while maillon.suivant.suivant != None:
                maillon = maillon.suivant
            """
            on a récupéré le maillon dont le suivant 
            du suivant est None
            ce maillon va devenir le nouveau premier 
            qd on supprimera le premier (en-dessous)
            """
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None


if __name__ == "__main__":
    F = File()
    print(F.est_vide())
    F.enfile(2)
    F.affiche()
    print(F.est_vide())
    F.enfile(5)
    F.enfile(7)
    F.affiche()
    print(F.defile())
    print(F.defile())
    F.affiche()
