let l = ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"];;

let encode l = 
  let rec aux c acc = function
  |[]->[]
  |[a]->(c+1,a)::acc
  |a::(b::_ as t)->
    if a=b then aux (c+1) acc t
    else aux 0 ((c+1,a)::acc) t in
  List.rev (aux 0 [] l);;