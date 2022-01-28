let conversion = function
  | "I" -> 1
  | "V" -> 5
  | "X" -> 10
  | "L" -> 50
  | "C" -> 100
  | "D" -> 500
  | "M" -> 1000
  | _ -> 0;;
let rec rom_to_dec = function
    | [] -> 0
    | [n] -> conversion n
    | (_ as h)::(_ as n) when conversion h >= conversion n -> conversion h + conversion n
    | (_ as h::(_ as n) when conversion h >= conversion n -> conversion n - conversion h
    | h::(n::_ as t) when conversion h >= conversion n -> conversion h + rom_to_dec t
    | h::(n::_ as t) when conversion h < conversion n -> rom_to_dec t - conversion h
    ;;
