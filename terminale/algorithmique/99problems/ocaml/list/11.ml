type 'a rle =
    | One of 'a
    | Many of int * 'a;;

let l = ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"];;

let encode l = 
  let rec aux c acc = function
  |[]->[]
  |[a]-> 
    if c=0 then One a::acc
    else Many (c+1,a)::acc
  |a::(b::_ as t)->
    if a=b then aux (c+1) acc t
    else aux 0 (Many (c+1,a)::acc) t in
  List.rev (aux 0 [] l);;