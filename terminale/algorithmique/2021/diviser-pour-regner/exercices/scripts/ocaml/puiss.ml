let rec puissance x n = 
  if n=0 
    then 1
    else 
      if n mod 2 = 0
        then puissance (x*x) (n/2)
        else x*puissance (x*x) (n/2);;