import doctest

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
        "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
        "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
        "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot):
    """
    vérifie si le mot est 'parfait'

    Args:
        mot (int): chaine de caractère

    Returns:
        bool: True si parfait

    >>> est_parfait("PAUL")
    [50, 1612112, False]
    >>> est_parfait("ALAIN")
    [37, 1121914, True]
    """
    # mot est une chaîne de caractères (en lettres majuscules)
    code_c = ""
    code_a = 0
    for c in mot:
        """
        accès à une variable globale!!! 
        mais seulement en lecture: on peut considérer que c'est une constante du programme
        """
        code_c = code_c + str(dico[c])
        code_a = code_a + dico[c]
    code_c = int(code_c)
    # code_c divisible code_a -> reste = 0
    if code_c % code_a == 0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    # le tableau contient des données hétérogènes: beurk, on aurait pu mettre un tuple
    return [code_a, code_c, mot_est_parfait]


if __name__ == "__main__":
    doctest.testmod(verbose=True)
