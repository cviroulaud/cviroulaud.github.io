//dans about:config mettre privacy.file_unique_origin à false

function loadSpe(adr) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", adr);
    xhr.responseType = "json";
    xhr.send();
    xhr.onload = function() {
        if (xhr.status != 200) {
            console.log("erreur" + xhr.status);
        } else {
            //createTab(this);
            //createTab(xhr.response); //objet json
            specialites = xhr.response;
            createTab();
        }
    }
}

function createTab() {
    //specialites = resp;
    console.log(specialites);
    tdImg = document.querySelector("#img-spe");
    tdDesc = document.querySelector("#td-desc");
    let tab = document.createElement("table");
    tab.setAttribute("id", "table-specialites");
    let tabDesc = document.querySelector("#table-desc");
    tabDesc.before(tab);

    for (let i = 0; i < specialites.length; i++) {
        let ligne;
        if (i % 3 == 0) { // nouvelle ligne
            ligne = document.createElement("tr");
            ligne.setAttribute("id", "ligne" + i / 3);
            tab.append(ligne);
        } else {
            ligne = document.querySelector("#table-specialites>tr:last-child");
        }
        let cel = document.createElement("td");
        cel.setAttribute("id", i);
        cel.innerHTML = specialites[i]["nom"];
        cel.addEventListener("click", callbackDesc);
        ligne.append(cel);
    }
}

function callbackDesc(e) {
    let nb = e.target.id;
    chgtImg("images/spe" + e.target.id + ".jpg", tdImg);
    tdDesc.innerHTML = specialites[nb]["description"];
}

// chgt image asynchrone
async function chgtImg(f, img) {
    let response = await fetch(f);
    let blob = await response.blob();
    img.src = URL.createObjectURL(blob);
}

let specialites;
let tdImg;
let tdDesc;
loadSpe("specialites.json");