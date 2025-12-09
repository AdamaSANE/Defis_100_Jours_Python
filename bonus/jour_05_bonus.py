# Bonus Jour 5 : Compte à rebours interactif avec choix de vitesse
import time

print("\n=== Compte à Rebours Interactif ===\n")
print("Bienvenue dans le défi bonus du Jour 5 ! 🕒")
print("À quelle vitesse souhaitez-vous le compte à rebours ?")
print("1. Demi-seconde (0.5s)")
print("2. Deux secondes (2s)")
print("3. Cinq secondes (5s)")
print("4. Personnalisé")

choix = input("Votre choix (1/2/3/4) : ")

if choix == "1":
	vitesse = 0.5
elif choix == "2":
	vitesse = 2
elif choix == "3":
	vitesse = 5
elif choix == "4":
	vitesse = float(input("Entrez la vitesse en secondes (ex: 1.5) : "))
else:
	print("Choix non reconnu, vitesse par défaut de 1 seconde.")
	vitesse = 1

nb_secondes = int(input("Combien de secondes pour le compte à rebours ? : "))

for i in range(nb_secondes, 0, -1):
	print(f"{i}...")
	time.sleep(vitesse)
print("🚀 C'est parti !")

print("\n=== Compte à Rebours Terminé ! ===\n")