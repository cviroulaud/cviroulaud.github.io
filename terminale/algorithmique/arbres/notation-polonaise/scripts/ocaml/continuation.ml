(* straightforward recursion *)
let rec sum s = 
  match s with
      [] -> 0
    | x::xs -> x + sum xs
(* tail recursive *)
let sum s =
let rec sum' s a =
  match s with
      [] -> a
    | x::xs -> sum' xs (a + x) in
  sum' s 0;;

  (*type intéressant (rien à voir)*)
  let funcomp f g x =
    g (f x);;
  
(* using continuations *)
let sum s =
let rec sum' s k =
  match s with
      [] -> k 0
    | x::xs -> sum' xs (fun a -> k (x + a)) in
sum' s (fun x -> x);;

let rec fact x n = 
  match n with
  | 0 -> 1
  | _ -> x * fact x (n-1);;

  print_int (fact 2 4);;

let fact_cont x n =
  let rec aux x n k =
    match n with
    | 0 -> k 1
    | _ -> aux x (n-1) (fun a -> k x*a) in
    aux x n (fun h->h);;
print_int (fact_cont 2 4);;