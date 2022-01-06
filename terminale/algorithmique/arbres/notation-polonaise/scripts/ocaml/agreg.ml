type tree = E | N of tree * tree;;
let rec height t = 
  match t with
  | E -> print_string "ok";0
  | N(l,r) -> print_string "ok";1+max (height l) (height r);;

(*height (N(N(E,N(E,E)),N(E,E)));;*)
let rec left t n =
  if n = 0 then t else left (N(t,E)) (n-1);;

let rec aux1 t k =
  match t with
  | E -> k 0
  | N(l,r) -> print_string "aux1N ";
            aux1 l (fun hl -> print_string "1 ";aux1 r (fun hr -> print_string "2 ";k (1+max hl hr)));;

let height1 t = print_string "deb ";aux1 t (fun h -> print_string "3 ";h);;
height1 (N(E,N(E,E)));;