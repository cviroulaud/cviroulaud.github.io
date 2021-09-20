let insert_at m n l = 
  let rec aux i = function
  |[] -> [m]
  |h::t as liste->
    if i=n then m::liste
    else h::aux (i+1) t in
    aux 0 l;;

let t = insert_at "alfa" 4 ["a"; "b"; "c"; "d"];;
let rec a = function
|[]->print_newline()
|h::t-> print_string h;a t;;
a t;;