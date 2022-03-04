let dicho tab e =
  let rec aux d f =
      if f>d then
      let m = (d+f)/2 in
      if tab.(m) = e then true
      else if tab.(m) > e then aux d (m-1) 
      else aux (m+1) f 
    else false in
  aux 0 (Array.length tab-1);;
let tab = [|1;2;4;6;7;9;10;11;14;15|];;
print_string (string_of_bool (dicho tab 13));;
print_string (string_of_bool (dicho tab 11));;