let rec somme n = 
  if n = 1
    then 1
    else somme (n-1) + n*n;;
print_int (somme 3);;