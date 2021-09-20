type 'a rle =
    | One of 'a
    | Many of int * 'a;;
let l= [Many (4, "a"); One "b"; Many (2, "c"); Many (2, "a"); One "d"; Many (4, "e")];;

let decode l =
  let rec ajoute a b acc=
  if a=0 then acc else ajoute (a-1) b (b::acc) in
  let rec aux acc = function
  |[]->acc
  |One a::t-> aux (a::acc) t
  |Many (a,b)::t-> aux (ajoute a b acc) t
     in
  List.rev (aux [] l);;