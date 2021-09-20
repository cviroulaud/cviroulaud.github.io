let permutation l = 
  let rec extract n acc = function
    | []-> raise Not_found
    | h::t -> 
      if n=0 then (h,acc@t)
      else extract (n-1) (h::acc) t in
  let rec aux acc liste = 
    let taille = List.length liste in
    if taille = 0 then acc
    else 
      let nb, rest = extract (Random.int taille) [] liste in
      aux (nb::acc) rest in
    aux [] l;;

let t = permutation ["a"; "b"; "c"; "d"; "e"; "f"];;
let rec a = function
|[]->print_newline()
|h::t-> print_string h;a t;;
a t;;