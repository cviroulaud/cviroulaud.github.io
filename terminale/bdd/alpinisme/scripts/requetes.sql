/*Donner pour chaque 1re ascension d'un sommet de plus de 8500 m le nom du grimpeur, le nom du sommet et son altitude ?*/
select s.nom, s.altitude, a.nom_grimpeur
from Sommet as s
join Ascension as a
on s.nom = a.nom_sommet
where s.altitude > 8500;

/*Nom des pays dont un grimpeur a réalisé la 1re ascension d'un sommet de plus 8000 m ?*/
select distinct pays
from Localisation;

/*Nom et prénom des grimpeurs ayant réalisé la 1re ascension d'un sommet de plus de 8000 m du Pakistan ?*/
select distinct nom_grimpeur, prenom_grimpeur
from Ascension
join Localisation
on Localisation.nom_sommet = Ascension.nom_sommet
where pays='Pakistan';

/*Nom et prénom des grimpeurs n'appartenant pas à un pays possédant un sommet de plus 8000 m ?*/
select nom, prenom
from Grimpeur
where pays not in 
	(select distinct pays 
	 from Localisation);

/*Nom des grimpeurs ayant réalisé une 1re ascension d'un sommet de plus de 8000 m avec Hermann Buhl ?*/
select nom_grimpeur
from Ascension as a1
where exists 
	(select nom_grimpeur
	from Ascension as a2
	where a2.nom_grimpeur = 'Bull' and
	a1.nom_grimpeur <> 'Bull' and
	a1.nom_sommet = a2.nom_sommet);

/*Nom des sommets de plus de 8500 m situés au Népal mais pas sur la frontière avec la Chine ?
(SELECT nom
 FROM Sommet
 WHERE altitude > 8500)
INTERSECT
  (SELECT nom_sommet
   FROM Localisation
   WHERE pays = 'Népal')
EXCEPT
  (SELECT nom_sommet
   FROM Localisation
   WHERE pays = 'Chine');
*/

/*Nombre de sommets de plus de 8000 m de chaque pays en possédant ?*/
select pays, count(*)
from Localisation
group by pays;

/*Donner pour chaque pays : son nom et le nombre de sommets de plus de 8000 m 
dont la 1re ascension a été réalisée par un grimpeur de ce pays. 
Trier le résultat par nombre décroissant de sommets ?*/

select pays, count(nom_sommet)
from Localisation
group by pays
having pays in 
	(select pays
	from Grimpeur);
