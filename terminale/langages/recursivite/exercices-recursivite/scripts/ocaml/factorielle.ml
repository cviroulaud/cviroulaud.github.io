let rec facto x = function
| 0 -> 1
| n -> x*facto x (n-1);;
print_int (facto 2 4);;