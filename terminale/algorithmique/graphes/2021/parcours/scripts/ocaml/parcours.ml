type matrice = int array array;;
type noeud = {mutable couleur:int; mutable dist:int; mutable pred:int};;
let mat : matrice = [|
  [|0; 0; 0; 0; 1; 0; 1; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0|];
  [|0; 0; 0; 0; 0; 1; 0; 1; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0|];
  [|0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0|];
  [|0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 1; 1; 1; 0; 0; 1; 0; 0; 0; 0|];
  [|1; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 1; 0; 1; 0; 0; 0; 0; 0|];
  [|0; 1; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0|];
  [|1; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 1; 1; 0; 0; 0; 0; 0|];
  [|0; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0|];
  [|0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 1; 0; 0; 0; 1|];
  [|0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0|];
  [|0; 0; 0; 1; 1; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 1; 0; 0; 0; 0|];
  [|0; 0; 1; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0|];
  [|0; 0; 0; 1; 1; 1; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 0; 0; 0|];
  [|0; 1; 0; 0; 0; 0; 1; 1; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 1|];
  [|1; 0; 0; 0; 1; 0; 1; 0; 1; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 1|];
  [|0; 0; 0; 1; 0; 0; 0; 0; 1; 0; 1; 1; 0; 0; 0; 0; 1; 0; 0; 0|];
  [|0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 1; 1; 1|];
  [|0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 1; 1|];
  [|0; 0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 0; 0; 1; 1; 0; 0|];
  [|0; 0; 0; 0; 0; 0; 0; 0; 1; 0; 0; 0; 0; 1; 1; 0; 1; 1; 0; 0|]
|];;

let parcours_dfs mat =
  let suivi = let elt i j = 0 in 
    let ligne i = Array.init 3 (elt i) in 
      Array.init 20 ligne in
  (*suivi.(0).dist=0 in*)
  let rec dfs n= 
    suivi.(n).(0)<-1;
    print_int n;
    print_string " ";
    for i=0 to 19 do
      if mat.(n).(i) = 1 then
        if suivi.(i).(0) = 0 then
          dfs i
    done;
    suivi.(n).(0)<-2 (*inutile*)
  in dfs 0;;
parcours_dfs mat;;

(*FAUX à cause de suivi: voir fin du fichier*)
let parcours_dfs2 mat  =
  let suivi = Array.make 20 (Array.make 3 0) in
  (*suivi.(0).dist=0 in*)
  let rec dfs n = 
    suivi.(n).(0)<-1;
    print_int n;
    print_string " ";
    for i=0 to 19 do
      if mat.(n).(i) = 1 then
        if suivi.(i).(0) = 0 then
          dfs i 
    done;
    suivi.(n).(0)<-2 (*inutile*)
  in dfs 0;;
parcours_dfs2 mat;;
(*FIN FAUX*)

(*test construction tableaux*)
print_newline();;

let tab2 =
  let t = Array.make 3 [||] in
  for i = 0 to 2 do 
    let ligne = Array.make 4 0 in
      t.(i) <- ligne
  done;    
    t ;;
for i=0 to 2 do
  for j=0 to 3 do
    print_int tab2.(i).(j)
  done;
  print_newline();
done;;
print_newline();;

tab2.(0).(2)<-3;;
for i=0 to 2 do
  for j=0 to 3 do
    print_int tab2.(i).(j)
  done;
  print_newline();
done;;
print_newline();;

print_string "faux: ";;
print_newline();;

(*FAUX: chaque ligne faire référence au même tableau!!*)
let tab3 = Array.make 3 (Array.make 4 0);;
tab3.(2).(0)<-1;;
for i=0 to 2 do
  for j=0 to 3 do
    print_int tab3.(i).(j)
  done;
  print_newline();
done;;
