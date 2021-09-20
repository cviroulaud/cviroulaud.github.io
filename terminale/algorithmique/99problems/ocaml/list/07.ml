type 'a node =
    | One of 'a 
    | Many of 'a node list;;
let l = [One "a"; 
          Many [One "b"; 
            Many [One "c" ;One "d"]; One "e"]];;

let flatten l= 
  let rec aux acc = function
    | []-> acc
    | One h::t-> aux (h::acc) t
    | Many h::t-> aux(aux acc h) t in
  aux [] l;; (*renvoie à l'envers; faire un List.rev*)