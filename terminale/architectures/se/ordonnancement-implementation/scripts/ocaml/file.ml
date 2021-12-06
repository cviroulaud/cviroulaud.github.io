exception Vide;;
type 'a cel = {x: 'a; 
                mutable pred: 'a maillon;
                mutable succ: 'a maillon}
and 'a maillon = Nil | Cellule of 'a cel;;
type 'a file = {mutable premier: 'a maillon; mutable dernier: 'a maillon};;
let creer()={premier= Nil; dernier=Nil};;
let enfiler f x = let c = Cellule {x=x; pred=f.dernier; succ=Nil} in
          match f.dernier with
          | Nil -> f.premier <- c; f.dernier <- c
          | Cellule n -> n.succ <- c; f.dernier <- c;;
let defiler f = match f.premier with
| Nil -> raise Vide
| Cellule h -> match h.succ with
| Nil -> f.premier <- Nil; f.dernier <- Nil; h.x
| Cellule n -> n.pred <- Nil;f.premier<-Cellule n;h.x;;

let f = creer();;
enfiler f 3;;
enfiler f 4;;
enfiler f 5;;
print_int (defiler f);;
print_int (defiler f);;
print_int (defiler f);;
print_int (defiler f);;