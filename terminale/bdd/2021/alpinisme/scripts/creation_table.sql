create table Localisation (
nom_sommet varchar(20),
pays varchar(20),
primary key (nom_sommet, pays),
FOREIGN KEY (nom_sommet) REFERENCES Sommet (nom));

create table Sommet (
nom varchar(20),
altitude int,
annee int,
face char(2),
primary key (nom));

create table Grimpeur (
nom varchar(20),
prenom varchar(20),
pays varchar(20),
primary key (nom,prenom));

create table Ascension (
nom_grimpeur varchar(20),
prenom_grimpeur varchar(20),
nom_sommet varchar(20),
primary key (nom_grimpeur, prenom_grimpeur, nom_sommet),
foreign key (nom_sommet) references Sommet (nom));
