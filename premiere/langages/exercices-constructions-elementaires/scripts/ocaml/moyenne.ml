(*let notes = Array.make 10 0;;
let complete tab = for i = 0 to 10
do
tab.(i)<-read_int();
done;;*)
let notes = let tab = Array.make 3 0 in
for i = 0 to 2
do
tab.(i)<-read_int();
done;tab;;
for i = 0 to 2
do
print_int notes.(i)
done;