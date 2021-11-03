/*let specialites = ["Histoire géographie, géopolitique et sciences politiques", "Humanités, littérature et philosophie",
    "Langues, littératures et cultures étrangères", "Littérature, langues et cultures de l’Antiquité", "Mathématiques",
    "Numérique et sciences informatiques", "Sciences de la vie et de la Terre", "Sciences de l’ingénieur",
    "Sciences économiques et sociales", "Physique chimie", "Arts : histoire des arts, théâtre, arts plastiques, arts du spectacle, etc",
    "Biologie écologie"]
    
let tab = document.createElement("table");*/

function creerTab(donnees) {
    let content = document.querySelector("#content");
    let tab = document.createElement("table");
    for (let i = 0; i < donnees.length; i++) {
        // créer ligne de 3 colonnes
        let ligne;
        if (i % 3 == 0) {
            ligne = document.createElement("tr");
            tab.append(ligne);
        } else {
            ligne = tab.lastChild;
        }
        // ajout cellule
        let col = document.createElement("td");
        col.append(donnees[i].nom);
        ligne.appendChild(col);
    }
    content.appendChild(tab);
}