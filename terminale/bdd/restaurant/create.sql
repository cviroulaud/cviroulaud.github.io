CREATE TABLE Restaurant(
rID integer,
nom varchar(50),
type varchar(30),
adresse varchar(50),
primary key (rID));

CREATE TABLE Evaluateur(
eID integer,
pseudonyme varchar(30),
dateInscription date,
primary key (eID));

CREATE TABLE Evaluation(
rID integer,
eID integer,
dateEval date,
note integer,
primary key (rID, eID, dateEval),
foreign key (rID) references Restaurant(rID),
foreign key (eID) references Evaluateur(eID));