function creerTab(donnees) {
    let content = document.querySelector("#content");
    let tab = document.createElement("table");
    let img = document.createElement("img");
    img.setAttribute("id", "img-spe");
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
        col.setAttribute("mImg", donnees[i].image);
        col.append(donnees[i].nom);
        ligne.appendChild(col);
    }
    content.appendChild(tab);
    content.appendChild(img);
    tab.addEventListener("click", function(e) {
        if (e.target.tagName == "TD") {
            let fImg = "images/" + e.target.getAttribute("mImg") + ".jpg";
            chgtImg(fImg, img);
        }
    });
}

// chgt image asynchrone
async function chgtImg(f, img) {
    let response = await fetch(f);
    let blob = await response.blob();
    img.src = URL.createObjectURL(blob);
}