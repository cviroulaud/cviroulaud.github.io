Random.self_init()
let loto n m =
  let rec verifier nb = function
  |[]->true
  |h::t->
    if nb=h then false
    else verifier nb t in
  let rec get_n deja=
    let nb = (Random.int 48)+1 in
    if verifier nb deja then nb
    else get_n deja in
  let rec aux i acc =
    if i=n then acc
    else aux (i+1) (get_n acc::acc) in
  aux 0 [];;

  let t = loto 6 49;;
  let rec a = function
  |[]->print_newline()
  |h::t-> print_int h;print_string " ";a t;;
  a t;;