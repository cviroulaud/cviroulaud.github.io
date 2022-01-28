let rec dernier = function
  | [] -> None
  | [h] -> Some h
  | h::t -> dernier t;;

let rec deux_der = function
  | [] -> None
  | [h;t] -> Some (h,t)
  | h::t -> deux_der t;;

let rec kieme n = function
  | [] -> None
  | h::t -> if n=1 then Some h else kieme (n-1) t;;

let rec length = function
  | [] -> 0
  | h::t -> 1 + length t;;

  (*
let rec reverse = function
  | [] -> []
  | h::t -> reverse t::Some h::[];;
  *)