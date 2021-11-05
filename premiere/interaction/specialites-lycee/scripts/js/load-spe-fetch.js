async function chargeJSON(fichier) {
    let response = await fetch(fichier);
    if (response.ok) { // if HTTP-status is 200-299
        let tab = await response.json();
        creerTab(tab);
        //alert(JSON.stringify(tab));
    } else {
        alert("HTTP-Error: " + response.status);
    }
}

chargeJSON("specialites.json");