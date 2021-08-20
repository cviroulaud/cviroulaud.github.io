let pair nb =
  for i = 0 to nb do if i mod 2 = 0 then 
    begin print_int i;print_string " "end done;;
pair 24;;