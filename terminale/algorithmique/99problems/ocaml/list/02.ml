let conv = function
| None -> 0
| Some (a,b) -> a*b;;

let l : int list = [1;2;3;4];;
let rec last = function
| [] | [_] -> None
| [a;b]-> Some (a,b)
| _::q -> last q;;
print_int (conv (last l));;
print_int (conv (last [5]));;