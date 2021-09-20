let t = [|1;3;4|];;
let iteration t = 
  let l :int array = [|0;0;0;0;0;0|] in
  Array.iter (fun x -> l.(x)<-1) t;
  for i=0 to 5 do print_int l.(i)done;; 
iteration t;;
 
print_newline();;
let t2 = [|1;2;3;4|];;

let t3 = Array.map (fun x->2*x) t2;;
for i=0 to 3 do print_int t3.(i)done;;  