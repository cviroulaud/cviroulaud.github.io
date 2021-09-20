let l = ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "d"; "e"; "e"; "e"; "e"];;

let pack acc = function
| a::(b::_ as t)-> if a=b then pack (a::b)