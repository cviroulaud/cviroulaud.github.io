let length_sort l =
  let rec mini l_min acc = function
  | [] -> (l_min, acc)
  | h::t ->
    if List.length h < List.length l_min then mini h (l_min::acc) t
    else mini l_min (h::acc) t in
  let rec aux  = function
  | [] -> []
  | h::t -> 
      let l_min,reste = (mini h [] t) in
      l_min::aux reste in
  aux l;;

  let t = length_sort [["a"; "b"; "c"]; ["d"; "e"]; ["f"; "g"; "h"]; ["d"; "e"];
  ["i"; "j"; "k"; "l"]; ["m"; "n"]; ["o"]];;
 