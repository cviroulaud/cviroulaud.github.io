let range d f = 
  let rec aux en_c = 
    if en_c < f then en_c::aux (en_c+1)
    else if en_c > f then en_c::aux (en_c-1)
    else [f] in
  aux d;;

  let rec a = function
|[]->print_newline()
|h::t-> print_int h;a t;;

let t = range 4 9;;
a t;;
let t2 = range 9 4;;
a t2;;
