class Combattant:
    """Crée un combattant avec ses caractéristiques propres"""
    def __init__(self,tenue,parachute,trainee):
        self.outfit=tenue
        self.glider=parachute
        self.contrail=trainee
        self.energy=100
        self.shield=100
        self.backpack=[]

    def get_outfit(self):
        return self.outfit

    def set_outfit(self,nouvelle):
        self.outfit=nouvelle

    def subir_attaque(self,degat):
        """
        modifie les PV et le bouclier du joueur en fonction des dégâts
        """
        if degat <= self.shield:
            self.shield -= degat
        else:
            if self.shield > 0:
                degat -= self.shield
                self.shield = 0
            self.energy -= degat

    def ramasser_objet(self,objet):
        if len(self.backpack) < 3:
            self.backpack.append(objet)
            return "Objet ajouté."
        else:
            return "Le sac est plein."

joueur1=Combattant("cuddle-team-leader","hot-rod","flames")
joueur2=Combattant("red-knight","hot-rod","all-star")
