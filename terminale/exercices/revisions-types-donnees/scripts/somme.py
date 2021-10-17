from random import randint

tup = tuple(randint(0, 100) for i in range(10))

def somme(tup: tuple) -> int:
    resultat = 0
    for element in tup:
        resultat += element
    return resultat

print(tup)
print(somme(tup))