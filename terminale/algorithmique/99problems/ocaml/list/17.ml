let split l n = 
  let rec aux i acc = function
  | []->(List.rev acc,[])
  | h::t->
    if i=n then (List.rev (h::acc),t)
    else aux (i+1) (h::acc) t in
  aux 1 [] l;;

  let t = split ["a"; "b"; "c"; "d"; "e"; "f"; "g"; "h"; "i"; "j"] 3;;
  let rec a = function
  |[]->print_newline()
  |h::t->print_string h;a t;;
  let (t1,t2)=t;;
  a t1;;
  a t2;;