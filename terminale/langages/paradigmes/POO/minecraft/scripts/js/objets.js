let pioche = {
    nom: "john",
    getAge() {
        return this.age;
    },
};
pioche["age"] = 12;


let affiche = function(obj) {
    for (let k in obj) {
        console.log(obj[k]);
    }
}
console.log(pioche.getAge());
affiche(pioche);


function Outil(nom) {
    this.nom = nom;
    this.force = 10;
}

let pioche2 = new Outil("pioche");
affiche(pioche2);

class Sol {
    constructor(t) {
        this.typ = t;
        this.durete = 10;
    }

    afficheType() {
        return this.typ;
    }

}

class Roche extends Sol {
    constructor(t) {
        super(t);
        this.gravier = false;
    }
}

let terre = new Sol("Terre");
console.log(terre.typ);

let roche = new Roche("rocher");
console.log(roche.typ);
console.log(roche instanceof Roche);
console.log(roche instanceof Sol);