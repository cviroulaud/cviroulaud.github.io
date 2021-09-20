let remove_at n l = 
  let rec aux i = function
  | []->[]
  | h::t->
      if i=n then t
      else h::aux (i+1) t in
    aux 0 l;;

let t = remove_at 1 ["a";"b";"c";"d"];;
let rec a = function
|[]->print_newline()
|h::t-> print_string h;a t;;
a t;;