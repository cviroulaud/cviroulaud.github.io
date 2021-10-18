let rec collatz n =
  if n = 1 then
    "oui"
  else
    begin
    print_int n;print_newline();
    if n mod 2 = 0 then
      collatz (n/2)
    else
      collatz (3*n+1)
    end;;

print_string (collatz 6);;
print_newline();;
let rec collatz2 n l=
  if n = 1 then
    l
  else
    begin
    if n mod 2 = 0 then
      collatz2 (n/2) (n::l)
    else
      collatz2 (3*n+1) (n::l)
    end;;

 let l = collatz2 6 [];;
 let rec affiche = function
 | [] -> print_string "fin";print_newline()
 | h::q -> print_int h; print_newline(); affiche q;;
 affiche l;;