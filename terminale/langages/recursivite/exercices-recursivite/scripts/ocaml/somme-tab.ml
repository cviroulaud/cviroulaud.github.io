Random.self_init ();;
let taille = 3;;
let t = let tab = Array.make taille 0 in
for i = 0 to taille-1
do
tab.(i)<-Random.int 10;(*entre 0 et 9*)
print_int tab.(i);
print_string " ";
done;tab;;
let rec somme t i = if i = Array.length t
  then 0
  else  t.(i)+somme t (i+1);;
print_int (somme t 0);;