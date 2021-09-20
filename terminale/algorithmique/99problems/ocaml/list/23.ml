let rand_select l n = 
  let rec get_n i = function
  |[]->" "
  |h::t->
    if i=n then h
    else get_n (i+1) t in

  let rec aux compt acc = 
    if compt=n then acc
    else aux (compt+1) (get_n (Random.int 8)::acc) in
  aux 0 [];;

  let t = rand_select ["a"; "b"; "c"; "d"; "e"; "f"; "g"; "h"] 3;;
  let rec a = function
  |[]->print_newline()
  |h::t-> print_string h;a t;;
  a t;;
  (*FAUX; voir correction, plusieurs points intéressants: 
                                      raise, 
                                      décomposition tuple*)