CREATE TABLE `Bandes_dessinees` (
  `serie` String,
  `titre` String,
  `tome` Integer,
  `isbn` String,
  `genre` String,
  `scenariste` String,
  `dessinateur` String,
  `editeur` String,
  `date_parution` Date
);

CREATE TABLE `Emprunteurs` (
  `prenom` String,
  `nom` String,
  `naissance` Date,
  `telephone` String
);

CREATE TABLE `Emprunteurs_2` (
  `prenom` String,
  `nom` String,
  `naissance` Date,
  `nb_emprunts` Integer
);
