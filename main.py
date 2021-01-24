# Demander le mot de passe
from getpass import getpass
from fonctions import *
import os


###Dans le cas ou le logiciel est lancé pour la premiere fois###
#Si jamais le fichier n'est pas existant, on le créer
try:
    fichier = open("mdp.txt", "r")
except FileNotFoundError:
    fichier = open("mdp.txt", "w")
    fichier.close()

fichier = open ("mdp.txt", "r")
text = fichier.read()
if text == "":
    print("C'est la première fois que vous lancez le logiciel de gestionnaire de mots de passe, entrez un"
          " mot de passe qui le sécurisera (il ne sera pas stocké):")
    mdp = input(">")
    fichier.close
    fichier = open ("mdp.txt", "w")
    fichier.write(encrypt(hashage(mdp), "debut".encode()).decode())
    fichier.close()
    quit()
###################################################################################

print("Version 1.0")
print("Mots de passes\n\n1.Stocker un mot de passe\n2.Voir tous les mots de passe")
choix = int(input(">"))

print("\nAvant toute chose, entrez le mot de passe : ")
#mdp = getpass()
mdp = input("mdp svp:")
mdp = hashage(mdp)

if verifier_mdp(mdp) is False:
    print("Il semble que ça ne soit pas le bon mot de passe, le dechiffrage est impossible!")
    os.system ("PAUSE")
    quit()

if choix == 1:
    while 1:
        service_compte = input ("Service auquel le compte est enregistré\n>")
        nom_compte = input("Nom du compte\n>")
        mdp_compte = input("Mot de passe du compte\n>")
        ajouter_fichier(mdp, nom_compte, mdp_compte, service_compte)
elif choix == 2:
    lire_fichier(mdp)
else:
    print("Erreur dans le choix")

os.system("PAUSE")


