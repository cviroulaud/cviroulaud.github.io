let rec pair nb = if nb>=0 then 
  if nb mod 2 = 0 then begin print_int nb;print_string " "; pair (nb-2)end
  else pair (nb-1);;
pair 25;;
