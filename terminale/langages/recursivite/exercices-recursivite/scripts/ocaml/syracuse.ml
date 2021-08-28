let rec syracuse u = 
    print_int u; print_string " ";
    if u > 1
      then if u mod 2 == 0
        then syracuse(u / 2)
        else syracuse (3 * u + 1);;
syracuse 5;;
  
