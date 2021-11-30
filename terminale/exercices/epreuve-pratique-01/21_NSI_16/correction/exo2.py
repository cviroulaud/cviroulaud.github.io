import doctest


def dec_to_bin(a):
    """
    écriture binaire d'un entier

    Args:
        a ([int]): l'entier

    Returns:
        [str]: écriture binaire

    LES TESTS NE SONT PAS DEMANDÉS DANS L'EXERCICE
    >>> dec_to_bin(83)
    '1010011'
    >>> dec_to_bin(127)
    '1111111'
    """
    bin_a = ""
    #a = a//2
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a//2
    return bin_a

print(dec_to_bin(10))
if __name__ == "__main__":
    doctest.testmod(verbose=True)
