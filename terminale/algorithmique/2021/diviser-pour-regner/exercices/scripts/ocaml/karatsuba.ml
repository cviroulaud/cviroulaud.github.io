open Puiss;;
let rec kara m1 m2 n = 
  if n=1
    then m1*m2
    else 
      let k = n/2 in
      let a = m1/(puissance 10 k) in
      let b = m1 mod (puissance 10 k) in
      let c = m2/(puissance 10 k) in
      let d = m2 mod (puissance 10 k) in
      let a0 = kara a c (n/2) in
      let a2 = kara b d (n/2) in
      let a1 = kara (a-b) (c-d) (n/2) in
      a0*(puissance 10 (2*k)) + (a0+a2-a1)*(puissance 10 k) + a2;;

print_int (kara 1237 2587 4);;
print_newline();;
