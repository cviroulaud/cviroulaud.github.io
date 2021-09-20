let conv = function
| None -> 0
| Some n -> n;;
let l : int list = [1;2;3;4];;
let rec dernier = function
  | [] -> None
  | [h] -> Some h
  | _::q -> dernier q;;
print_int (conv (dernier l));;

let rec dernier_int = function
  | [] -> 0
  | [h] -> h
  | _::q -> dernier_int q;;
print_int (dernier_int l);;