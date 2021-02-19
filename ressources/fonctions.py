#Fonctions du programme de cryptage
import hashlib

from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet, InvalidToken


def hashage(mdp: str):
    mdp_tableau = []
    for i in range(len(mdp)):
        mdp_tableau.append("0")
        mdp_tableau[i] = mdp[i]
    for i in range(1,10):
        mdp_tableau.append("#")
        mdp_tableau.append("@")
    mdp = "".join(mdp_tableau)
    mdp = hashlib.sha256(mdp.encode()).hexdigest()[:44]
    return mdp[:43] + "="


def encrypt(key: bytes, text: bytes):
    return Fernet(key).encrypt(text)


def decrypt(key: bytes, text: bytes):
    return Fernet(key).decrypt(text)


def ajouter_fichier(cle, nom_compte, mdp_compte, service_compte):
    text = encrypt(cle.encode(), "{}|{}|{}".format(service_compte, nom_compte, mdp_compte).encode())

    fichier = open("ressources/mdp.txt", "a")
    fichier.write(f"\n{text.decode()}")
    fichier.close()


def lire_fichier(cle):
    fichier = open("ressources/mdp.txt", "r")
    text = fichier.read().split("\n")
    identifiants_groupes = []

    try:
        for info in text:
            identifiants_groupes.append(decrypt(cle, info.encode()).decode())
    except InvalidSignature:
        print("Le mot de passe n'est pas bon!")
    except InvalidToken:
        print("Erreur dans le décodage des mots de passe, ce n'est surement pas le bon mot de passe!")
    a_retourner = []
    for info in identifiants_groupes:
        identifiants = info.split("|")
        if info == "debut":
            None
        else:
            a_retourner.append(identifiants)
    return a_retourner


def verifier_mdp(mdp):
    fichier = open("ressources/mdp.txt", "r")
    text = fichier.read().split("\n")
    identifiants_groupes = []

    try:
        for info in text:
            identifiants_groupes.append(decrypt(mdp, info.encode()).decode())
    except InvalidSignature:
        return False
    except InvalidToken:
        return False
    return True







