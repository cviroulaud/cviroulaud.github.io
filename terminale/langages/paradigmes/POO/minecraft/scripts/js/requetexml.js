let formulaire = FormData(document.forms.form1);
let xhr = new XMLHttpRequest();
xhr.responseType = "json";
xhr.open("POST", "url");
xhr.send(formulaire);

xhr.onload = function() {
    if (xhr.status != 200) {
        alert("erreur" + xhr.status);
    } else {
        alert(xhr.response);
    }
}

//plusieurs appels
loadDoc("url-1", myFunction1);

loadDoc("url-2", myFunction2);

function loadDoc(url, cFunction) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        cFunction(this);
    }
    xhttp.open("GET", url);
    xhttp.send();
}

function myFunction1(xhttp) {
    // action goes here
}

function myFunction2(xhttp) {
    // action goes here
}

// fetch

async function loadScript(adr) {
    let response = await fetch(adr);
    if (!response.ok) {
        alert("erreur" + response.status);
    } else {
        let json = await response.json();
    }
}