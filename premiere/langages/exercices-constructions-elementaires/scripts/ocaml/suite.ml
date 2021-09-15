let rec suite n =
  if n = 0
    then 42.
    else (suite (n-1))**(1./.3.)+.2.;;
print_float (suite 3);;

print_newline();;
let rec suite2 a n = 
  if n=0
    then a
    else
      begin
        let v = suite2 a (n-1) in
        0.5*.(v+.a/.v)
      end;;
print_float (suite2 3. 4);;
print_newline();;