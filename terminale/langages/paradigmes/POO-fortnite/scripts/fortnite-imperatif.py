combattant={"outfit":"cuddle-team-leader", "glider":"glider", "contrail":"flames",
            "back_bling":"royale-shield", "emote":"disco-fever",
            "pickaxe":"pick-squeak", "toy":"tomato"}

combattant={"outfit":"cuddle-team-leader", "glider":"glider", "contrail":"flames",
            "back_bling":"royale-shield", "emote":"disco-fever",
            "pickaxe":"pick-squeak", "toy":"tomato", "backpack":[]}

combattant={"outfit":"cuddle-team-leader", "glider":"glider", "contrail":"flames",
            "back_bling":"royale-shield", "emote":"disco-fever",
            "pickaxe":"pick-squeak", "toy":"tomato", "backpack":[],
            "energy":100, "shield":100}

for cle in combattant.keys():
    print(cle,end=" ")

for item in combattant.values():
    print(item,end=" ")

for item in combattant.items():
    print(item,end=" ")

def subir_attaque(degat,joueur):
    """
    modifie les PV et le bouclier du joueur en fonction des dégâts
    """
    if degat <= joueur["shield"]:
        joueur["shield"] -= degat
    else:
        if joueur["shield"] > 0:
            degat -= joueur["shield"]
            joueur["shield"] = 0
        joueur["energy"] -= degat

def ramasser_objet(objet,joueur):
    """
    Ajoute un objet dans le sac s'il n'est pas plein.
    """
    if len(joueur["backpack"]) < 3:
        joueur["backpack"].append(objet)
        return "Objet ajouté."
    else:
        return "Le sac est plein."


print("PV: {} Bouclier:{}".format(combattant["energy"],combattant["shield"]))
subir_attaque(30,combattant)
print("PV: {} Bouclier:{}".format(combattant["energy"],combattant["shield"]))
subir_attaque(80,combattant)
print("PV: {} Bouclier:{}".format(combattant["energy"],combattant["shield"]))

print(combattant["backpack"])
print(ramasser_objet("burst-assault-rifle",combattant))
print(combattant["backpack"])