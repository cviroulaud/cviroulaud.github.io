Random.self_init ();;
(* marche pas!! voir https://stackoverflow.com/questions/7536633/ocaml-pattern-matching-vs-if-else-statements
dans le match, 'de' fait référence à un pattern et non à la variable précédente
  let lancer () = let rec demande de = match read_int() with
    | de -> Printf.printf "%s" "gagné"
    | _-> demande de
in demande (Random.int 5 + 1);;
lancer ();;
*)
let lancer () = let de = Random.int 5 + 1 in 
let rec demande nb = if read_int () = de then
  Printf.printf "%d" nb
else demande (nb+1) in
demande 1;;
lancer();; 