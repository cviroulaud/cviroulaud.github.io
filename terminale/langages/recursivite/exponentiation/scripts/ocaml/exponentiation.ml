let rec exponentiation x = function
| 0 -> 1
| n -> x*exponentiation x (n-1);;
print_int (exponentiation 6 4);;
print_string "\n";;

let rec expo1 x n = if n=0 then 1
else x*expo1 x (n-1);;
print_int (expo1 6 4);;
print_string "\n";;

let rec expo2 x n = if n = 0 then 1 
else if n mod 2 = 0 then expo2 (x*x) (n/2)
  else x*expo2 (x*x) (n/2);; (*la division renvoie un entier comme // en python*)
print_int (expo2 6 4);;
print_string "\n";;

let rec expo3 x = function
| 0 -> 1
| n -> if n mod 2 = 0 then expo2 (x*x) (n/2)
else x*expo2 (x*x) (n/2);;
print_int (expo3 6 4);;
print_string "\n";;