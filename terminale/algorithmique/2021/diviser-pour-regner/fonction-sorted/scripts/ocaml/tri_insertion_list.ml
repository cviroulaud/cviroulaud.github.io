
let rec affiche = function
|[]->print_newline()
| h::t -> print_int h;affiche t;;
let rec insere x = function
| []->[x]
| h::t as l-> if h<x then h::insere x t else x::l;;

let rec tri_insertion acc = function
    | []-> acc
    | h::t -> tri_insertion (insere h acc) t;;
let l1 = [3;9;8;1;10;2];;
print_string "tri insertion";;
affiche (tri_insertion [] l1);;