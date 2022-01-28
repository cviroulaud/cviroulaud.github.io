type sommet = int;;
type poids = float;;
type graphe = (sommet list) array;;
type graphe_p = ((sommet * poids) list) array;;

let g1 : graphe = [|
  [3];
  [3];
  [4];
  [0;1;5];
  [2;5];
  [3;4;6];
  [5]
|];;
let g2 : graphe_p = [|
  [(3,2.)];

|];;
let t : (int*int)array = [|
  (1,2)
|];;
print_int (let (a,b)= t.(0) in b);;

type mat_p = (poids option) array array;;
let mat : mat_p = [|
  [|None;None;None;Some 4.|];
|];;