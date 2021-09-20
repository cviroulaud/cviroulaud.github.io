let duplicate l =
  let rec aux acc = function
  |[]->acc
  |h::t->aux (h::h::acc) t in
List.rev (aux [] l);;

let l = duplicate [1;2;3;4];;
let rec affiche = function
|[]-> print_string "\n"
|h::t->print_int h;affiche t;;
affiche l;;

 