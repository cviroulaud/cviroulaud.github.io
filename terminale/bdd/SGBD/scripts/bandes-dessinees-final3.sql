PRAGMA foreign_keys = ON;

CREATE TABLE `Bandes_dessinees` (
  `serie` Text,
  `titre` Text,
  `tome` Integer,
  `isbn` Integer PRIMARY KEY,
  `id_genre` Integer,
  `id_scenariste` Integer,
  `id_dessinateur` Integer,
  `id_editeur` Integer,
  `date_parution` Date,
FOREIGN KEY (`id_scenariste`) REFERENCES `Auteurs` (`id`),
FOREIGN KEY (`id_dessinateur`) REFERENCES `Auteurs` (`id`)
);

CREATE TABLE `Editeurs` (
  `id` Integer PRIMARY KEY,
  `editeur` Text,
FOREIGN KEY (`id`) REFERENCES `Bandes_dessinees` (`id_editeur`)
);

CREATE TABLE `Genres` (
  `id` Integer PRIMARY KEY,
  `genre` Text,
FOREIGN KEY (`id`) REFERENCES `Bandes_dessinees` (`id_genre`)
);

CREATE TABLE `Auteurs` (
  `id` Integer PRIMARY KEY,
  `prenom` Text,
  `nom` Text
);

CREATE TABLE `Emprunteurs` (
  `id` Integer PRIMARY KEY,
  `prenom` Text,
  `nom` Text,
  `naissance` Date
);

CREATE TABLE `Emprunts` (
  `isbn` Integer PRIMARY KEY,
  `id_emprunteurs` Integer,
FOREIGN KEY (`isbn`) REFERENCES `Bandes_dessinees` (`isbn`),
FOREIGN KEY (`id_emprunteurs`) REFERENCES `Emprunteurs` (`id`)
);
