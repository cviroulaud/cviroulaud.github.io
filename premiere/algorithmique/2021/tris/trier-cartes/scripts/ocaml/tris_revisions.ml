let rec inserer e = function
  | [] -> [e]
  | h::t when e > h -> h::inserer e t
  | h::t as l -> e::l;; 
let rec tri_insertion acc = function
  | [] -> acc
  | h::t -> tri_insertion (inserer h acc) t;;
let rec affiche = function
  |[]->print_newline()
  | h::t -> print_string ((string_of_int h)^"-");affiche t;;
let l1 = [3;9;8;1;10;2];;
print_string "tri insertion";;
affiche (tri_insertion [] l1);;

