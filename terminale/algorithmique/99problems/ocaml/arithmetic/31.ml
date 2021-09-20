let isprime n = 
  if n<=2 then true
  else let rec divby i = 
    if i*i>=n then true
    else if n mod i = 0 then false
    else divby (i+1) in
  divby 2;;

  let crible n =
    let rec range i =
      if i=n then [n]
      else i::range (i+1) in
    let entiers = range 2 in
    let rec creer div= function
      |[] -> []
      |h::t -> 
        if h mod div = 0 then creer div t
        else h::creer div t in
    let rec aux acc  = function
      | [] -> []
      | h::t as l->
        if h*h>n then (List.rev l)@acc
        else aux (h::acc) (creer h t) in
      List.rev (aux [] entiers);;
