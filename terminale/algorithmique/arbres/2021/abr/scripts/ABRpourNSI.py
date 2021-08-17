from graphviz import Digraph

INDENTATION = "  "

class ABR:
    '''Un ABR référence un noeud ou rien. On suppose qu'un ABR ne peut
       contenir qu'une seule occurrence de chaque valeur.'''
    def __init__(self, racine = None):
        self.racine = racine

    def __str__(self):
        if self.est_vide():
            representation = "Arbre Vide !"
        else:
            representation = self.racine.to_string("")
        return representation

    def est_vide(self):
        return self.racine is None

    def visu(self):
        '''Méthode permettant d'avoir une représentation graphique
           de l'arbre grâce à graphviz'''
        assert not(self.est_vide())
        graphe = Digraph()
        self.racine.ajoute_noeud_visu(graphe)
        graphe.render("arbre", view=True)

    def rechercher(self, valeur):
        '''Si la valeur est présente dans l'arbre, elle est renvoyée,
        sinon, on renvoie la valeur None. Renvoyer la valeur plutôt que
        True permet de faire une recherche via une clé.'''
        if self.est_vide():
            trouve = None
        else:
            trouve = self.racine.rechercher(valeur)
        return trouve
        
    def inserer(self, valeur):
        '''Insertion d'une valeur dans l'arbre.'''
        if self.est_vide():
            self.racine = Noeud(valeur)
        else:
            self.racine.inserer(valeur)

    def supprimer(self, valeur):
        '''Suppression d'une valeur dans l'arbre. La méthode suppression
        de la classe Noeud renvoie un arbre car il se peut que la valeur
        à supprimer soit celle du noeud racine ; il faut alors que le
        noeud référencé par self.racine soit modifié.'''
        if self.est_vide():
            return
        else:
            self.racine = self.racine.supprimer(valeur)

class Noeud:
    '''Classe représentant un noeud dans un ABR. Un noeud est
    caractérisé par une valeur, un noeud gauche et un noeud droit.'''
    def __init__(self, valeur, noeud_gauche = None, noeud_droit = None):
        self.valeur = valeur
        self.noeud_gauche = noeud_gauche
        self.noeud_droit = noeud_droit

    def to_string(self, decalage):
        '''Représentation textuelle d'un ABR : les sous-arbres sont
        représentés l'un sous l'autre avec un décalage spécifié par la
        variable globale INDENTATION. Les noeuds vides sont représentés
        par un X.'''
        retour = decalage
        retour += str(self.valeur) + "\n"
        if self.est_feuille():
            return retour
        if self.noeud_gauche is None:
            retour += decalage + INDENTATION + "X\n"
        else:
            retour += self.noeud_gauche.to_string(decalage + INDENTATION) 
        if self.noeud_droit is None:
            retour += decalage + INDENTATION + "X\n"
        else:
            retour += self.noeud_droit.to_string(decalage + INDENTATION)
        return retour

    def est_feuille(self):
        return self.noeud_gauche is None and self.noeud_droit is None

    def ajoute_noeud_visu(self, graphe, parent = None, etiquette = None):
        '''méthode utilisée pour représenter un arbre graphiquement
        graphe à graphviz.'''
        noeud = str(self.valeur)
        graphe.node(noeud)
        if not(parent is None):
            graphe.edge(parent, noeud, label=etiquette)
        if not(self.noeud_gauche is None):
            self.noeud_gauche.ajoute_noeud_visu(graphe, noeud, "<")
        if not(self.noeud_droit is None):
            self.noeud_droit.ajoute_noeud_visu(graphe, noeud, ">")        
        
    def rechercher(self, valeur):
        '''méthode permettant de rechercher une valeur dans l'arbre.
        Si on trouve la valeur, on la renvoie. Sinon, on renvoie None.'''
        if self.valeur == valeur:
            return self.valeur
        elif valeur < self.valeur:
            if self.noeud_gauche is None:
                return None
            else:
                return self.noeud_gauche.rechercher(valeur)
        else:
            if self.noeud_droit is None:
                return None
            else:
                return self.noeud_droit.rechercher(valeur)

    def inserer(self, valeur):
        '''Méthode permettant d'insérer une valeur dans une ABR.'''
        if valeur < self.valeur:
            if self.noeud_gauche is None:
                self.noeud_gauche = Noeud(valeur)
            else:
                self.noeud_gauche.inserer(valeur)
        elif valeur > self.valeur:
            if self.noeud_droit is None:
                self.noeud_droit = Noeud(valeur)
            else:
                self.noeud_droit.inserer(valeur)

    def supprimer(self, valeur):
        '''Méthode permettant de supprimer une valeur dans un ABR.
        Il s'agit d'un problème algorithmiquement assez difficile
        Quand le noeud à supprimer a 2 fils. C'est pourquoi on
        fait appel à une méthode intermédiaire : supprimer_noeud_courant.
        À noter : la méthode supprimer, contrairement à la méthode 
        ajouter, renvoie un arbre, qu'il faut donc ré-affecter au
        fils concerné.'''
        if valeur < self.valeur:
            self.noeud_gauche = self.noeud_gauche.supprimer(valeur)
            return self
        elif valeur > self.valeur:
            self.noeud_droit = self.noeud_droit.supprimer(valeur)
            return self
        else:
            return self.supprimer_noeud_courant()

    def supprimer_noeud_courant(self):
        '''Méthode permettant de supprimer le noeud courant. Si le noeud
        a 0 ou 1 fils, c'est plutôt simple. Sinon, on peut, par exemple,
        remplacer la valeur du noeud courant par la plus petite valeur
        du sous-arbre droit, mais il faut alors supprimer le noeud feuille
        contenant cette valeur. Ce travail est dévolu à la méthode
        chercher_et_supprimer_min.'''
        if self.est_feuille():
            return None
        elif self.noeud_gauche is None:
            return self.noeud_droit
        elif self.noeud_droit is None:
            return self.noeud_gauche
        else:
            (valeur, noeud) = self.noeud_droit.chercher_et_supprimer_min()
            self.valeur = valeur
            self.noeud_droit = noeud
            return self

    def chercher_et_supprimer_min(self):
        if not(self.noeud_gauche is None):
            (valeur, noeud) = self.noeud_gauche.chercher_et_supprimer_min()
            self.noeud_gauche = noeud
            return (valeur, self)
        else:
            return (self.valeur, None)

# Construction d'un ABR avec des entiers
n9 = Noeud(9)
n7 = Noeud(7, None, n9)
n13 = Noeud(13)
n11 = Noeud(11,n7, n13)
n3 = Noeud(3)
n2 = Noeud(2, None, n3)
n5 = Noeud(5, n2, n11)
arbre = ABR(n5)

# Construction d'un ABR de personnes ; recherche et tri faits sur l'identifiant.
class Personne1:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return self.prenom + " " + self.nom + " [" + str(self.id) + "]"

    def __eq__(self, autre):
        return self.id == autre.id

    def __lt__(self, autre):
        return self.id < autre.id

    def __gt__(self, autre):
        return self.id > autre.id

p1 = Personne1(1, "Miterrand", "François")
p2 = Personne1(3, "Sarkozy", "Nicolas")
p3 = Personne1(2, "Chirac", "Jacques")
p4 = Personne1(5, "Macron", "Emmanuel")
p5 = Personne1(4, "Hollande", "François")

arbre2 = ABR()
arbre2.inserer(p1)
arbre2.inserer(p2)
arbre2.inserer(p3)
arbre2.inserer(p4)
arbre2.inserer(p5)
print(arbre2)


# Construction d'un ABR de personnes ; recherche et tri faits sur (nom, prénom).
class Personne2:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return self.prenom + " " + self.nom + " [" + str(self.id) + "]"

    def __eq__(self, autre):
        return self.nom == autre.nom \
            and self.prenom == autre.prenom \
            and self.id == autre.id

    def __lt__(self, autre):
        return self.nom < autre.nom or \
               (self.nom == autre.nom and self.prenom < autre.prenom) or \
               (self.nom == autre.nom and self.prenom == autre.prenom and self.id < autre.id)

    def __gt__(self, autre):
        return self.nom > autre.nom or \
               (self.nom == autre.nom and self.prenom > autre.prenom) or \
               (self.nom == autre.nom and self.prenom == autre.prenom and self.id > autre.id)

p21 = Personne2(1, "Miterrand", "François")
p22 = Personne2(3, "Sarkozy", "Nicolas")
p23 = Personne2(2, "Chirac", "Jacques")
p24 = Personne2(5, "Macron", "Emmanuel")
p25 = Personne2(4, "Hollande", "François")

arbre3 = ABR()
arbre3.inserer(p21)
arbre3.inserer(p22)
arbre3.inserer(p23)
arbre3.inserer(p24)
arbre3.inserer(p25)
print(arbre3)
