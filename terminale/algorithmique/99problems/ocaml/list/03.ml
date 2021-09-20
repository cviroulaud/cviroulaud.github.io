let conv = function
|None->0
|Some a->a;;

let l:int list = [1;2;3;4];;
let rec k_ieme n = function
    | []-> None
    | h::q-> if n=1 then Some h else k_ieme (n-1) q;;
print_int (conv (k_ieme 3 l));;