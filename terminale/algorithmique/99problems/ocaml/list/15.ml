let l = [1;2;3];;
let replicate l n = 
  let rec rep acc i x =
    if i=0 then acc else rep (x::acc) (i-1) x in
  let rec aux acc = function
|[]->acc
|h::t-> aux (rep acc n h) t in
  aux [] (List.rev l);;
let res = replicate l 3;;
let rec affichage = function
|[]->print_string "\n"
|h::t->print_int h;affichage t;;
affichage res;;