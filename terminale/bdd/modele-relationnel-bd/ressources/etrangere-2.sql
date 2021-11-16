CREATE TABLE `Bandes_dessinees` (
  `serie` String,
  `titre` String,
  `tome` Integer,
  `isbn` Integer PRIMARY KEY,
  `id_genre` Integer
);

CREATE TABLE `Emprunteurs` (
  `id` Integer PRIMARY KEY,
  `prenom` String,
  `nom` String,
  `naissance` Date
);

CREATE TABLE `Emprunts` (
  `isbn` Integer PRIMARY KEY,
  `id_emprunteurs` Integer
);

CREATE TABLE `Genre` (
  `id_genre` Integer PRIMARY KEY,
  `genre` String
);

ALTER TABLE `Bandes_dessinees` ADD FOREIGN KEY (`isbn`) REFERENCES `Emprunts` (`isbn`);

ALTER TABLE `Emprunteurs` ADD FOREIGN KEY (`id`) REFERENCES `Emprunts` (`id_emprunteurs`);

ALTER TABLE `Genre` ADD FOREIGN KEY (`id_genre`) REFERENCES `Bandes_dessinees` (`id_genre`);
