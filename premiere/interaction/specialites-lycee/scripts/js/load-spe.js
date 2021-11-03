let xhr = new XMLHttpRequest();
xhr.open("GET", "specialites.json");
xhr.responseType = "json";
xhr.send();

//Dès que la réponse est reçue...
xhr.onload = function () {
    //Si le statut HTTP n'est pas 200...
    if (xhr.status != 200) {
        //...On affiche le statut et le message correspondant
        alert("Erreur " + xhr.status + " : " + xhr.statusText);
        //Si le statut HTTP est 200, on affiche le nombre d'octets téléchargés et la réponse
    } else {
        let tab = xhr.response;
        creerTab(tab);
        //alert(xhr.response.length + " octets  téléchargés\n" + JSON.stringify(xhr.response));
    }
};

//Si la requête n'a pas pu aboutir...
xhr.onerror = function () {
    alert("La requête a échoué");
};

//Pendant le téléchargement...
xhr.onprogress = function (event) {
    //lengthComputable = booléen; true si la requête a une length calculable
    if (event.lengthComputable) {
        //loaded = contient le nombre d'octets téléchargés
        //total = contient le nombre total d'octets à télécharger
        alert(event.loaded + " octets reçus sur un total de " + event.total);
    }
};