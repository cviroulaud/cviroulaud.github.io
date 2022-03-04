function chgtSpe(fichier) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", fichier);
    xhr.responseType = "json";
    xhr.send();
    xhr.onload = function() {
        if (xhr.status != 200) {
            alert("error");
        } else {
            let resultat = xhr.response;
            creerListe(resultat);
        }
    }
}

function creerListe(res) {
    let l = document.querySelector("ul[lis='spe']");
    for (let i = 0; i < res.length; i++) {
        let e = document.createElement("li");
        let t = document.createTextNode(res[i]["nom"]);
        //e.innerHTML = res[i]["nom"];
        e.append(t);
        l.append(e);
    }
}
chgtSpe("specialites.json");

async function chgtImg(img, balise) {
    let req = await fetch(img);
    if (req.ok) {
        let res = await req.blob();
        balise.src = URL.createObjectURL(res);
    }

}
let i = document.querySelector("#i");
i.addEventListener("click", function(e) {
    chgtImg("images/educ-nat.png", e.target);
});
chgtImg("images/bandeau.jpg", i);