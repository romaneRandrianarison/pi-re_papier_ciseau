import tkinter as tk
import random

def jouer(choix_user):
    choix_ordi = random.choice(["pierre", "papier", "ciseaux"])
    resultat = ""

    if choix_user == choix_ordi:
        resultat = "Égalité !"
    elif (choix_user == "pierre" and choix_ordi == "ciseaux") or \
         (choix_user == "papier" and choix_ordi == "pierre") or \
         (choix_user == "ciseaux" and choix_ordi == "papier"):
        resultat = "Tu as gagné ! 🎉"
    else:
        resultat = "L'ordinateur a gagné. 😞"

    label_resultat.config(text=f"Toi : {choix_user}\nOrdi : {choix_ordi} \n {resultat}")

fenetre = tk.Tk()
fenetre.title("Pierre-Papier-Ciseaux")
fenetre.geometry("300x200")

label_resultat = tk.Label(fenetre, text="Fais ton choix :", font=("Helvetica", 14))
label_resultat.pack(pady=20)

frame_boutons = tk.Frame(fenetre)
frame_boutons.pack()

for choix in ["pierre", "papier", "ciseaux"]:
    bouton = tk.Button(frame_boutons, text=choix.capitalize(), width=10, command=lambda c=choix: jouer(c))
    bouton.pack(side="left", padx=10)

fenetre.mainloop()
