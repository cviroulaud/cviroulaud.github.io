Random.self_init();;
let deviner () = let nb = Random.int 10 in
let rec chercher n = 
  if read_int ()=nb then print_int n
  else chercher (n+1);
in chercher 1;;
deviner();;