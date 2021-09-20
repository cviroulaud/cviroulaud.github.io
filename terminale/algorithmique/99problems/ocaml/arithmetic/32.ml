let rec pgcd a b =
  if a=0 then b
  else pgcd (b mod a) a;;
print_int (pgcd 5 10);;

let rec pgcd2 a b =
  if b=0 then a
  else pgcd2 b (a mod b);;
  print_int (pgcd2 10 5);;
