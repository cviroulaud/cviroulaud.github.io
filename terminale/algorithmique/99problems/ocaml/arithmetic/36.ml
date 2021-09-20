let isprime n = 
  if n<=2 then true
  else let rec divby i = 
    if i*i>=n then true
    else if n mod i = 0 then false
    else divby (i+1) in
  divby 2;;
let factors m = 
  let rec compte i m ite=
    if m mod i = 0 then compte i (m/i) (ite+1)
    else (m,ite) in
  let rec aux m i acc =
    if m=1 then acc
    else
      if isprime i then
        if m mod i = 0 then let rest,ite = compte i m 0 in aux rest i ((ite,i)::acc)
        else aux m (i+1) acc
      else aux m (i+1) acc in
    aux m 2 [];;