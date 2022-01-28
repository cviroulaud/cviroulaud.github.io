function load_pok(source) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", source);
    xhr.responseType = "json";
    xhr.send();
    xhr.onload = function() {
        if (xhr.status != 200) {
            alert(xhr.status);
        } else {
            pokemons = xhr.response["pokemon"];
            creerTab();
        }
    };
}

async function load_pok2(source) {
    let response = await fetch(source);
    if (response.ok) {
        let json = await response.json();
        pokemons = json["pokemon"];
        creerTab();
    } else {
        alert(response.status);
    }
}

function creerTab() {
    let tab = document.querySelector("#photos");
    let ligne;
    let cel;
    for (let i = 0; i < pokemons.length; i++) {
        if (i % 10 == 0) {
            ligne = document.createElement("tr");
            tab.append(ligne);
        }
        cel = document.createElement("td");
        let image = document.createElement("img");
        image.setAttribute("src", "img/" + pokemons[i]["name"] + ".png");
        image.setAttribute("id", pokemons[i]["id"]);
        image.addEventListener("click", callbackImage);
        cel.append(image);
        ligne.append(cel);
    }
}

function callbackImage(e) {
    let identifiant = e.target.getAttribute("id") - 1;
    let tab = document.querySelector("#fiche");

    let image = document.createElement("img");
    image.setAttribute("src", "img/" + pokemons[identifiant]["name"] + ".png");
    let tdImg = document.querySelector("tr:nth-child(1)>td:nth-child(1)");

    let titre = tab.querySelector("tr:nth-child(2)>td:nth-child(2)");
    titre.innerHTML = "<span>" + pokemons[identifiant]["name"] + "</span>";
}

let pokemons;
//load_pok("pokedex.json");
load_pok2("pokedex.json");