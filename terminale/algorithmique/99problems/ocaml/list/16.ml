(*drop de 3 en 3*)
let drop l =
  let rec aux acc = function
  |[] -> acc
  |[a]-> a::acc
  |[a;b]->a::b::acc
  |a::b::c::t-> a::b::(aux acc t) in
  aux [] l;;

let t = ["a"; "b"; "c"; "d"; "e"; "f"; "g"; "h"; "i"; "j"];;
let rec affi = function
|[]->print_newline()
|h::t->print_string h;affi t;;
affi (drop t);;

(*drop de n en n; version terminale*)
let drop2 l n = 
  let rec aux acc i = function
  |[]->acc
  |h::t->
    if i=0 then aux acc (n-1) t
    else aux (h::acc) (i-1) t in
  aux [] (n-1) l;;
  affi (List.rev (drop2 t 3));;