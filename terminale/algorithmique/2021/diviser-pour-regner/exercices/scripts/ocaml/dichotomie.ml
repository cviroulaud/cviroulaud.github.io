let rec dicho t x d f= 
if f<d then -1 else begin
let m=(d+f)/2 in if t.(m)=x then m
else if x<t.(m) then dicho t x d (m-1)
else dicho t x (m+1) f end;;

print_int (dicho [|1;2;4;6;8;9;10|] 8 0 6);;
print_int (dicho [|1;2;4;6;8;9;10|] 7 0 6)