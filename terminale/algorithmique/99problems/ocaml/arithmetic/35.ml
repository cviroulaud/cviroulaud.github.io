let isprime n = 
  if n<=2 then true
  else let rec divby i = 
    if i*i>=n then true
    else if n mod i = 0 then false
    else divby (i+1) in
  divby 2;;
let factors m = 
  let rec aux m i acc =
    if m=1 then acc
    else
      if isprime i then
        if m mod i = 0 then aux (m/i) i (i::acc)
        else aux m (i+1) acc
      else aux m (i+1) acc in
    aux m 2 [];;