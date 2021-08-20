Random.self_init ();;
let de = Random.int 5 + 1;;
let demande d = let nb = ref 0 in let proposition = ref 0 in
  while !proposition != d 
  do
    nb := !nb+1;
    proposition := Scanf.scanf " %d" (fun x -> x)
  done;Printf.printf "%d" !nb;;
demande de;;