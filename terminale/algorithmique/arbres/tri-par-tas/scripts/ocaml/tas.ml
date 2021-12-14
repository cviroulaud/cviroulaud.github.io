type 'a tas ={mutable taille: int; contenu: 'a array};;
let t : int tas= {taille=0; contenu=Array.make 10 0};;
t.taille = 1;;
t.contenu.(0)<-1;;