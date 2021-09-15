type objet={valeur:int;poids:int};;
let objets = 
  [|
    {valeur=0;poids=0};
    {valeur=1;poids=2};
    {valeur=2;poids=5};
    {valeur=3;poids=7};
    {valeur=7;poids=12};
    {valeur=10;poids=9};
|];;
let poids_max = 15;;
(*marche pas! bug dans les indices? tester avec un tab à 1D?*)
let solutions = Array.make 6 (Array.make (poids_max+1) 0);;
for i=1 to 5 do
  for j=1 to poids_max do 
    begin   
    let prend_pas = solutions.(i-1).(j) in
    if objets.(i).poids<=j then
      begin
      let prend = solutions.(i-1).(j-objets.(i).poids)+objets.(i).valeur in
      if prend > prend_pas then
        solutions.(i).(j)<-prend
      else
        solutions.(i).(j)<-prend_pas
      end
    else
        solutions.(i).(j)<-prend_pas
    end
      done;
    done;;

(*affichage*) 
for i=0 to 5 do
  for j=1 to poids_max do
    print_int solutions.(i).(j);
    print_string " "
  done;
  print_newline();
done;;