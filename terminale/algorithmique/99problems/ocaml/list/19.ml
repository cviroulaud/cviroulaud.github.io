let rotate l n = 
  let rec aux acc i = function
  |[]->List.rev acc
  |h::t->
    if i=n then t@List.rev acc
    else aux (h::acc) (i+1) t in
  aux [] 0 l;;

let t = rotate ["a"; "b"; "c"; "d"; "e"; "f"; "g"; "h"] 3;;
let rec a = function
|[]->print_newline()
|h::t->print_string h;a t;;
a t;;