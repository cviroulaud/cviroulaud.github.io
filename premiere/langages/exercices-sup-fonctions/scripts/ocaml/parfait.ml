let est_parfait n = 
  let rec aux n i =
    if n = i then
      0
    else
      if n mod i = 0 then
        i + aux n (i+1)
      else aux n (i+1) in
  if aux n 1 = n then "oui" else "non";;

print_string (est_parfait 6);;
print_string (est_parfait 28);;
print_string (est_parfait 18);;