let l: int list = [1;2;3;4];;
let rec length = function
| []->0
| _::t->1+length t;;
print_int (length l);;

let rec length_terminale n = function
| []->n
| _::t->length_terminale (n+1) t;;
print_int (length_terminale 0 l);;

(*encore mieux avec une fonction qui encapsule*)
let length2 list =
  let rec aux n = function
    | [] -> n
    | _ :: t -> aux (n + 1) t
  in aux 0 list;;