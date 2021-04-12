//référencement des noeuds du DOM
let cellule = document.getElementById("td-desc");
let tabSpecialites = document.getElementById("table-specialites");

//Définition du contenu pour chaque spécialité
let specialites = new Map();
specialites.set("spe0","Histoire géographie, géopolitique et sciences politiques");
specialites.set("spe1","Humanités, littérature et philosophie");
specialites.set("spe2","Langues, littératures et cultures étrangères");
specialites.set("spe3","Littérature, langues et cultures de l’Antiquité");
specialites.set("spe4","Mathématiques");
specialites.set("spe5","La spécialité Numérique et Sciences Informatiques vous permet de comprendre les bases de la programmation, pour élaborer des logiciels par exemple, des sites internet, des applications pour smartphones, etc.");
specialites.set("spe6","Sciences de la vie et de la Terre");
specialites.set("spe7","Sciences de l’ingénieur");
specialites.set("spe8","Sciences économiques et sociales");
specialites.set("spe9","Physique chimie");
specialites.set("spe10","Arts : histoire des arts, théâtre, arts plastiques, arts du spectacle, etc");
specialites.set("spe11","Biologie écologie");

//Écouteur sur le tableau
tabSpecialites.addEventListener('click', function(event) {
  //Récupération du l'id de la cellule cliquée
  var idSpe= event.target.getAttribute("id");
  //Modification du contenu de la cellule
  cellule.textContent=specialites.get(idSpe);
});
