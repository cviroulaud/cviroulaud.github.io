//référencement des noeuds du DOM
let cellule = document.getElementById("td-desc");
let tabSpecialites = document.getElementById("table-specialites");

let image = document.getElementById("img-spe");


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

//Définition de l'image de chaque spécialité
let images = new Map();
images.set("spe0","images/spe0.jpg");
images.set("spe1","images/spe1.jpg");
images.set("spe2","images/spe2.jpg");
images.set("spe3","images/spe3.jpg");
images.set("spe4","images/spe4.jpg");
images.set("spe5","images/spe5.jpg");
images.set("spe6","images/spe6.jpg");
images.set("spe7","images/spe7.jpg");
images.set("spe8","images/spe8.jpg");
images.set("spe9","images/spe9.jpg");
images.set("spe10","images/spe10.jpg");
images.set("spe11","images/spe11.jpg");


//Écouteur sur le tableau
tabSpecialites.addEventListener('click', function(event) {
  //Récupération du l'id de la cellule cliquée
  var idSpe= event.target.getAttribute("id");
  //Modification du contenu de la cellule
  cellule.textContent=specialites.get(idSpe);

  //Modification de l'image
  image.setAttribute("src",images.get(idSpe));
});
