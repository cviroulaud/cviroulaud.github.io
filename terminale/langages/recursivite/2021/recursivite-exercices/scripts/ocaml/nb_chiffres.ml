let rec nb_chiffres n = if n<10 then 1 else 1 + nb_chiffres(n/10);;
print_int (nb_chiffres 1234);;

(*version terminale*)
let nb_chiffres2 n = 
  let rec nb_term x acc = 
  if x<10 then acc else nb_term (x/10) (acc+1)
in nb_term n 1;;
print_int (nb_chiffres2 1234);;

