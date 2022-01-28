let euro_poids = [29; 29; 29; 29; 27; 13; 12; 12; 12; 10; 10; 7; 7; 7; 4];;
let votes = [true;true;false;true;false;false;false;true;true;false;true;false;false;false;false];;
let total_votes poids vote =
  let rec aux acc p v=
    match p,v with
      | [],[]->acc
      | [],_| _,[]->acc
      | h1::t1,h2::t2 -> if h2 then aux (h1+acc) t1 t2 else aux acc t1 t2 in
    aux 0 poids vote;;
print_int (total_votes euro_poids votes);;
print_newline();;
let rec total_votes_cont p v k =
    match p,v with
      | [],[]-> k 0
      | [],_| _,[]-> k 0
      | h1::t1,h2::t2 -> if h2 
          then total_votes_cont t1 t2 (fun a -> h1 + k a)
          else total_votes_cont t1 t2 (fun a -> k a);;
print_int (total_votes_cont euro_poids votes (fun h->h));;
print_newline();;
let resultats p v m = (total_votes p v)>=m;;
print_string (string_of_bool (resultats euro_poids votes 169));;
print_newline();;
let euro_populations =
  [82164; 59623; 59225; 57679; 39441; 15863; 10545;
  10239; 9997; 8861; 8102; 5330; 5171; 3776; 435];;
let pop_votes1 poids popu = 
  let rec aux acc p pop =
    match p, pop with
    | [],[]-> acc
    | _,[]|[],_->failwith "erreur"
    |h1::t1,h2::t2->aux (float_of_int h1/. float_of_int h2::acc) t1 t2 in
    aux [] poids popu;;
