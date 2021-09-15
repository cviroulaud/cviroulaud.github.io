let rec f n =
  if n > 100 then n - 10 
  else (print_int n;print_newline();f (f (n + 11))) ;;
print_int (f 3);;