exception Empty;;
type 'a pile = {mutable tab: 'a list};;
let creer () = {tab = []};;
let empiler p x = p.tab <- x::p.tab;;
let depiler p = match p.tab with
| [] -> raise Empty
| h::t -> p.tab <- t; h;;

let p = creer();;
empiler p 3;;
empiler p 4;;
print_int (depiler p);;