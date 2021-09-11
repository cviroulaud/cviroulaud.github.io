Random.self_init();;

let affiche t = let j = 0 in 
                      let rec affiche_rec t i = if i<Array.length t then 
                              begin print_int t.(i);
                                    print_string " ";
                                    affiche_rec t (i+1) end 
                                  in affiche_rec t j;print_string "\n";;

print_string "tri sélection\n";;
let tab = Array.init 10 (fun i -> Random.int 100);;
affiche tab;;

let tri_selection t = for i = 0 to Array.length t -1
                            do
                            let mini = ref i in
                            for j=i+1 to Array.length t -1
                            do
                            if t.(j)<t.(!mini) then mini := j
                            done;
                            let temp = t.(!mini) in
                            t.(!mini)<-t.(i);
                            t.(i)<-temp
                          done;;
tri_selection tab;;
affiche tab;;

print_string "tri sélection rec\n";;
let tab = Array.init 10 (fun i -> Random.int 100);;
affiche tab;;
let tri_selection_rec t = let swap i j = let temp = t.(i) in t.(i)<-t.(j);t.(j)<-temp
                in let rec selectionner i j mini =
                  if j < Array.length t then
                    if t.(j)<t.(mini) then
                      selectionner i (j+1) j
                    else
                      selectionner i (j+1) mini
                    else swap mini i
                    in 
                        let rec parcourir i =
                      if i < Array.length t then
                        begin
                        selectionner i (i+1) i;
                        parcourir (i+1)
                        end
                      in parcourir 0;;
tri_selection_rec tab;;
affiche tab;;
