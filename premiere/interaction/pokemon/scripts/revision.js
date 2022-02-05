function chargement(src) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", src);
    xhr.responseType = "json";
    xhr.send();
    xhr.onload = function() {
        if (xhr.status == 200) {
            rep = xhr.response;
            for (let i = 0; i < rep.length; i++) {
                console.log(rep[i]["name"]);
            }
        } else {
            alert(xhr.status);
        }
    };
}

async function dwl(src) {
    let rep = await fetch(src);
    if (rep.ok) {
        let fichier = await rep.json();
        for (let i = 0; i < fichier.length; i++) {
            console.log(fichier[i]["name"]);
        }
    } else {
        alert(rep.status);
    }
}
dwl("revision.json");