Random.self_init();;

let affiche t = let j = 0 in 
                      let rec affiche_rec t i = if i<Array.length t then 
                              begin print_int t.(i);
                                    print_string " ";
                                    affiche_rec t (i+1) end 
                                  in affiche_rec t j;print_string "\n";;

print_string "tri rapide\n";;
let tab = Array.init 10 (fun i -> Random.int 100);;
affiche tab;;

let tri_rapide t = let partitionner deb fin = 