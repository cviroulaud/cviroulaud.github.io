type formule = Vrai | Faux | Conjonction of formule * formule;;
let rec evalue = function
| Vrai -> true
| Faux -> false
| Conjonction (Faux, f2) -> false
| Conjonction (f1, Faux) -> false
| Conjonction (f1, f2) -> evalue f1 && evalue f2;;

print_string (string_of_bool 
  (evalue (Conjonction (
      Conjonction (Vrai,Vrai),
      Faux))));;

type t_note =
| Absent
| Maths of float
| Programmation of float;;

let n = Maths 4.;;
let n2 = Absent;;