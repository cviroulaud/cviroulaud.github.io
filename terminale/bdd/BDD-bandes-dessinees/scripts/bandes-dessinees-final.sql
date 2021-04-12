CREATE TABLE `Bandes_dessinees` (
  `serie` VARCHAR(40),
  `titre` VARCHAR(40),
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
  `editeur` VARCHAR(40),
FOREIGN KEY (`id`) REFERENCES `Bandes_dessinees` (`id_editeur`)
);

CREATE TABLE `Genres` (
  `id` Integer PRIMARY KEY,
  `genre` VARCHAR(40),
FOREIGN KEY (`id`) REFERENCES `Bandes_dessinees` (`id_genre`)
);

CREATE TABLE `Auteurs` (
  `id` Integer PRIMARY KEY,
  `prenom` VARCHAR(40),
  `nom` VARCHAR(40)
);

CREATE TABLE `Emprunteurs` (
  `id` Integer PRIMARY KEY,
  `prenom` VARCHAR(40),
  `nom` VARCHAR(40),
  `naissance` Date
);

CREATE TABLE `Emprunts` (
  `isbn` Integer PRIMARY KEY,
  `id_emprunteurs` Integer,
FOREIGN KEY (`isbn`) REFERENCES `Bandes_dessinees` (`isbn`),
FOREIGN KEY (`id_emprunteurs`) REFERENCES `Emprunteurs` (`id`)
);
