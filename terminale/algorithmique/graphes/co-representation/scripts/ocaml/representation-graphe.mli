type sommet = int
type poids = float
type graphe = sommet list array
type graphe_p = (sommet * poids) list array
val g1 : graphe
val g2 : graphe_p
val t : (int * int) array
type mat_p = poids option array array
val mat : mat_p
