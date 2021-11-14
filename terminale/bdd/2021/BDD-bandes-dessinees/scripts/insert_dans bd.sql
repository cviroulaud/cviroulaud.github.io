select bd.serie, bd.titre, bd.tome, bd.isbn, bd.date_parution, Genres.id, Auteurs.id, Auteurs2.id,Editeurs.id
from bd
join Genres on bd.genre=Genres.genre
join Auteurs on bd.nom_s=Auteurs.nom and bd.prenom_s=Auteurs.prenom
join Auteurs2 on bd.nom_d=Auteurs2.nom and bd.prenom_d=Auteurs2.prenom
join Editeurs on bd.editeur=Editeurs.editeur;