Random.self_init();;

let affiche t = let j = 0 in 
                      let rec affiche_rec t i = if i<Array.length t then 
                              begin print_int t.(i);
                                    print_string " ";
                                    affiche_rec t (i+1) end 
                                  in affiche_rec t j;print_string "\n";;

print_string "tri insertion\n";;
let tab = Array.init 10 (fun i -> Random.int 100);;
affiche tab;;
let tri_insertion t = 
  let swap i j = let temp = t.(i) in t.(i)<-t.(j);t.(j)<-temp
    in for i = 0 to Array.length t -1
        do
        let j= ref i in
        while !j-1 >=0 && t.(!j)<t.(!j-1)
          do
          swap !j (!j-1);
          decr j
          done;
        done;;
tri_insertion tab;;
affiche tab;;

print_string "tri insertion rec\n";;
let tab = Array.init 10 (fun i -> Random.int 100);;
affiche tab;;
let tri_insertion_rec t = let swap i j = let temp = t.(i) in t.(i)<-t.(j);t.(j)<-temp
in let rec place_elt j = if j-1 >= 0 && t.(j)<t.(j-1) 
                            then begin 
                              swap j (j-1);
                              place_elt (j-1)
                            end
                          in for i = 0 to Array.length t -1
                          do
                          let j= ref i in
                          place_elt !j
                        done;;

tri_insertion_rec tab;;
affiche tab;;

print_string "tri insertion rec rec\n";;
let tab = Array.init 10 (fun i -> Random.int 100);;
affiche tab;;
let tri_insertion_rec_rec t = let swap i j = let temp = t.(i) in t.(i)<-t.(j);t.(j)<-temp
in let rec place_elt j = if j-1 >= 0 && t.(j)<t.(j-1) 
                            then begin 
                              swap j (j-1);
                              place_elt (j-1)
                            end
                          in let rec chaque_elt l = if l < Array.length t
                            then begin
                               let k= ref l in
                                place_elt !k;
                                chaque_elt (l+1)
                            end 
                          in chaque_elt 0;;
tri_insertion_rec_rec tab;;
affiche tab;;