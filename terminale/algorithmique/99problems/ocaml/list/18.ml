let slice l d f =
  let rec coupe acc long = function
    |[]->List.rev acc
    |h::t-> 
      if long = f-d then List.rev (h::acc)
      else coupe (h::acc) (long+1) t in
  let rec aux deb = function
  |[]->[]
  |h::t as complet->
    if deb=d then coupe [] 0 complet
    else aux (deb+1) t in
  aux 0 l;;

  let t = slice ["a"; "b"; "c"; "d"; "e"; "f"; "g"; "h"; "i"; "j"] 2 6;;
  let rec a = function
  |[]->print_newline()
  |h::t->print_string h;a t;;
  a t;;