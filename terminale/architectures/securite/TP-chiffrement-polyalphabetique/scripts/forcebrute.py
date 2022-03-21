from xor import creer_cle_bin, appliquer_xor, bin_en_int, chiffrement, dechiffrement


def get_fin(message: list, taille: int) -> list:
    fin = []
    for i in range(taille, 0, -1):
        fin.append(message[len(message)-i])
    return fin


def forcebrute(secret_bin: list, mot_connu: str) -> str:
    deb = ord("A")
    fin = ord("Z")+1
    fin_message_bin = get_fin(secret_bin, len(mot_connu))
    for l1 in range(deb, fin):
        for l2 in range(deb, fin):
            for l3 in range(deb, fin):
                # création de la clé
                cle = chr(l1)+chr(l2)+chr(l3)
                cle_bin = creer_cle_bin(cle, len(secret_bin))
                fin_cle_bin = get_fin(cle_bin, len(mot_connu))
                # tentative de décryptage avec cette clé
                fin_message_bin = appliquer_xor(fin_message_bin, fin_cle_bin)
                fin_message = ""
                for lettre_bin in fin_message_bin:
                    fin_message = fin_message+chr(bin_en_int(lettre_bin))
                
                # comparaison de la fin du message
                if fin_message == mot_connu:
                    print(cle)
                    print(fin_message)
                    return dechiffrement(secret_bin, cle)
    return "Message non décrypté!"


message = "ECEMESSAGEESTCOURTMAISVOUSNELETROUVEREZPASTOF"
secret_bin = chiffrement(message, "JDB")
print(secret_bin)
print(forcebrute(secret_bin, "TOF"))