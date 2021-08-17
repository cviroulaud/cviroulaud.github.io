let tri_insertion l = 
  let swap i j = let t = l.(i) in l.(i)<-l.(j);l.(j)<-t
in for i = 1 to Array.length l - 1 do
  let j = ref (i-1)
in while !j >= 0 && l.(!j)>l.(!j+1) do
  swap (!j) (!j+1);
  decr j
done
done;;
let a = [|3;1;4;9;8|];;
tri_insertion a;;
(*for i=0 to Array.length a -1 do
  print_int a.(i)done;;*)
let rec print_list a i = 
  if i<Array.length a then 
   begin print_int a.(i) ; print_string " " ; print_list a (i+1)end;;

print_list a 0;;

let tri_selection l = 
  let swap i j = let t = l.(i) in l.(i)<-l.(j);l.(j)<-t in
  for i = 0 to Array.length l - 1 do
    let mini = ref i in
    for j = i+1 to Array.length l - 1 do
      if l.(j) < l.(!mini) then mini := j
      done;
    swap i !mini 
  done;;
  let a = [|3;1;4;9;8|];;
  tri_selection a;;
  print_list a 0;;
