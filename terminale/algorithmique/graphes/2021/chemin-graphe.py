from queue import *

g2 = {
'A': ['B','E'],
'B': ['A','C','E'],
'C': ['B'],
'D': [],
'E': ['A','B']
}

g3 = {
'A': ['B'],
'B': ['A','C','E'],
'C': ['B'],
'D': [],
'E': ['B']
}

def affiche(chemin):
    ch = ""
    if len(chemin) == 0:
        return ch
    ch=str(chemin[0])
    for i in range (1,len(chemin)):
        ch=ch + " --> " + chemin[i]
    return ch

def chemins(graphe,dep,arr):
    file = Queue()
    file.put((dep,[dep]))
    while file.qsize() > 0:
        sommet,chemin = file.get()
        for s in graphe[sommet]:
            if s not in chemin:
                if s==arr:
                    yield chemin + [s] # Génére le nouveau chemin
            else:
                file.put((s,chemin+[s]))
    return chemin

c = chemins(g2,"A","E")
for a in c:
    print(affiche(chemin))