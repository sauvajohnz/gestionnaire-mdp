from tkinter import *
from tkinter.messagebox import *
from ressources.fonctions import *

fenetre = Tk() #on créer la fenetre

#caracteristiques de la fenetre
fenetre.title("Gestionnaire de mots de passe")
fenetre.geometry("1000x600")
fenetre.minsize(1000,600)
fenetre.maxsize(1000,600)
fenetre.iconbitmap("ressources/logo_cadena.ico")
fenetre.config(background="#4065A4")

#######################composants de la fenetre######################################
#canvas
canvas = Canvas(fenetre, width=0, height=0)
filename = PhotoImage(file= "ressources/cadena2.png")
background_label = Label(fenetre, image=filename)
background_label.place(x=0,y=0, relwidth=1, relheight=1)
#titre
label_titre = Label(fenetre, text="Gestionnaire de mots de passe", font=("Helvetica", 35), bg="#4065A4", fg="white")
#soustitre
label_soustitre = Label(fenetre, text="Entrez le mot de passe maître:", font=("Helvetica", 21), background="#4065A4", fg="white")
#entree
mdp_input = Entry(fenetre, font=("Helvetica", 21), bg="#4065A4", fg="white", width=17, show="*", bd="1", insertbackground="white")



def lancerProgramme(event): #On lance le coeur du programme !
    mdp = mdp_input.get()
    mdp = hashage(mdp)
    # On test si le mot de passe est correct
    if verifier_mdp (mdp) is False:
        print ("incorrectpw")
        showerror("Gestionnaire de mots de passe", "Le mot de passe est incorrecte!")
        fenetre.destroy()
    else:
        print("correctpw")
        fenetre.withdraw()
        fenetre_identifiants = Toplevel(fenetre)
        # caracteristiques de la fenetre
        fenetre_identifiants.title ("Gestionnaire de mots de passe")
        fenetre_identifiants.geometry ("600x400")
        fenetre_identifiants.minsize (600, 400)
        fenetre_identifiants.maxsize (600, 400)
        fenetre_identifiants.iconbitmap("ressources/logo_cadena.ico")
        fenetre_identifiants.config (background="#4065A4")
        #fenetre_identifiants.rowconfigure(5, weight=1)
        #fenetre_identifiants.columnconfigure(3, weight=1)

        #composants de la fenetre

        #la liste
        liste_identif = Listbox(fenetre_identifiants, height="20", width="15", font=("Helvetica", 13))
        liste_identif.grid(row=0, column=0, rowspan=25, columnspan=2)

        #les 2 labels
        label_identifiant = Label(fenetre_identifiants, text="Identifiant = ", font=("Helvetica", 16), bg="#4065A4", fg="white", width="42", anchor='nw')
        label_mdp = Label(fenetre_identifiants, text="Mot de passe = ", font=("Helvetica", 16), bg="#4065A4", fg="white", width="42", anchor='nw')
        label_identifiant.grid(row=0, column=4, columnspan=2)
        label_mdp.grid(row=1, column=4, columnspan=2)

        #les 3 input
        service_input = Entry(fenetre_identifiants, font=("Helvetica", 12), bg="#4065A4", fg="white", bd="1", insertbackground="white", width=36)
        username_input = Entry(fenetre_identifiants, font=("Helvetica", 12), bg="#4065A4", fg="white", bd="1", insertbackground="white", width=36)
        motdepasse_input = Entry(fenetre_identifiants, font=("Helvetica", 12), bg="#4065A4", fg="white", show="*", bd="1", insertbackground="white", width=36)

        #On les assignes dans la grid
        service_input.grid(row=10, column=4)
        username_input.grid(row=11, column=4)
        motdepasse_input.grid(row=12, column=4)

        #On leur met un texte prédéfinit
        service_input.insert(0, "Service(ex:Netflix)")
        username_input.insert(0, "Nom d'utilisateur/Email")
        motdepasse_input.insert(0, "Mot de passe")

        identifiants = []
        def crypter_identifiants():
            ajouter_fichier(mdp, username_input.get(), motdepasse_input.get(), service_input.get())
            liste_identif.insert(liste_identif.size()+1, service_input.get())
            identifiants.append([service_input.get(), username_input.get(), motdepasse_input.get()])

        # le bouton
        bouton_ajouter = Button (fenetre_identifiants, text="Ajouter le compte", command=crypter_identifiants, bg="white")
        bouton_ajouter.grid (row=13, column=4)

        #les valeurs de la liste
        tableau_identif = lire_fichier(mdp)
        i = 1
        for infos in tableau_identif:
            if infos == "debut":
                None
            else:
                identifiants.append(infos)
                liste_identif.insert(i, infos[0])
                i += 1

        def event_listbox(event):
            selection = event.widget.curselection()
            try:
                selection = int(selection[0])
                label_identifiant.config(text=f"Identifiant = {identifiants[selection][1]}")
                label_mdp.config (text=f"Mot de passe = {identifiants[selection][2]}")
            except IndexError: #Au cas ou l'on ne selectionne aucune case de la liste, selection renvoie () et ça créer une erreur IndexError.
                pass

        liste_identif.bind("<<ListboxSelect>>", event_listbox)

        fenetre_identifiants.mainloop()

fenetre.bind ("<Return>", lancerProgramme)

######################################################################################################################################################################
#####################Dans le cas ou le logiciel est lancé pour la premiere fois#######################################################################################
######################################################################################################################################################################
#Fonction qui assigne le mot de passe récupéré sur l'applicaiton
def assigner_nv_mdp(event):
    mdp = mdp_input.get ()
    fichier = open ("ressources/mdp.txt", "w")
    fichier.write(encrypt(hashage(mdp), "debut".encode()).decode())
    fichier.close()
    showinfo("Message", "Relancez le programme!")
    fenetre.destroy()

#On regarde si le fichier mdp existe, s'il existe pas c'est que c'est la première fois que le programme est lancé
try:
    fichier = open("ressources/mdp.txt", "r")
except FileNotFoundError:
    fichier = open("ressources/mdp.txt", "w") #On créer le fichier mdp
    fichier.close()

fichier = open("ressources/mdp.txt", "r")
text = fichier.read()
if text == "": #S'il n'y a rien dans ce fichier mdp, c'est la première fois qu'on a lancé le programme, on attend que l'utilisateur rentre le mot de passe
    fichier.close()

    #On en profite pour designer d'une manière différente l'application lors du premier démarrage
    #le fond d'écran
    filename = PhotoImage(file="ressources/cadena1.png")
    background_label = Label (fenetre, image=filename)
    background_label.place (x=0, y=0, relwidth=1, relheight=1)
    #les widgets
    label_titre = Label(fenetre, text="Creation du mot de passe maître", font=("Helvetica", 35), bg="#117141", fg="white")
    label_soustitre = Label(fenetre, text="Saissisez le ci-dessous:", font=("Helvetica", 21), background="#117141",fg="white")
    mdp_input = Entry(fenetre, font=("Helvetica", 21), bg="#117141", fg="white", width=17, show="*", bd="1", insertbackground="white")
    fenetre.bind("<Return>", assigner_nv_mdp)
else: #S'il y a quelque chose c'est que le programme est déjà fonctionnel
    fichier.close()
    fenetre.bind ("<Return>", lancerProgramme)  # On associe la touche "Entrer" à la confirmation du mot de passe
######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################


#On affecte les widgets a l'application
label_titre.pack(side="top", padx="1", pady="100")
label_titre.focus_set()
label_soustitre.pack(side="top", padx="1", pady="1")
mdp_input.pack(side="top", padx="1", pady="5")
canvas.pack()


#on affiche la fenetre
fenetre.mainloop()