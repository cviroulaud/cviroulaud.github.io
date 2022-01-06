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

(*continuation*)
let length3 list =
  let rec aux k = function
  | [] -> k 0
  | h::t -> aux (fun a -> 1 + k a) t in
  aux (fun h -> h) list;;

  print_int (length3 l);;
