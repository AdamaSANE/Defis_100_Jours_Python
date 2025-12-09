
# Bonus Jour 7 : Liste de courses avec modification, sauvegarde et chargement
import os

# Nom du fichier où la liste est sauvegardée
FICHIER_LISTE = "liste_courses.txt"

# Charge la liste de courses depuis le fichier
def charger_liste():
	if os.path.exists(FICHIER_LISTE):
		with open(FICHIER_LISTE, "r", encoding="utf-8") as f:
			return [ligne.strip() for ligne in f if ligne.strip()]
	return []

# Sauvegarde la liste de courses dans le fichier
def sauvegarder_liste(liste):
	with open(FICHIER_LISTE, "w", encoding="utf-8") as f:
		for item in liste:
			f.write(item + "\n")

# Affiche la liste de courses à l'utilisateur
def afficher_liste(liste):
	print("\nVotre liste de courses :")
	for idx, item in enumerate(liste, 1):
		print(f"{idx}. {item}")

# Permet de modifier un article existant
def modifier_article(liste):
	afficher_liste(liste)
	num = input("Numéro de l'article à modifier : ")
	if num.isdigit():
		num = int(num)
		if 1 <= num <= len(liste):
			nouveau = input(f"Nouveau nom pour '{liste[num-1]}' : ")
			liste[num-1] = nouveau
			print("Article modifié !")
		else:
			print("Numéro invalide.")
	else:
		print("Entrée non valide.")

# Fonction principale de l'application
def main():
	liste = charger_liste()
	print("Bienvenue dans votre gestionnaire de liste de courses ! 🛒")
	while True:
		print("\nMenu :")
		print("1. Afficher la liste")
		print("2. Ajouter un article")
		print("3. Modifier un article")
		print("4. Supprimer un article")
		print("5. Quitter et sauvegarder")
		choix = input("Votre choix : ")
		if choix == "1":
			afficher_liste(liste)
		elif choix == "2":
			item = input("Nom de l'article à ajouter : ")
			liste.append(item)
			print("Article ajouté !")
		elif choix == "3":
			if liste:
				modifier_article(liste)
			else:
				print("La liste est vide.")
		elif choix == "4":
			afficher_liste(liste)
			num = input("Numéro de l'article à supprimer : ")
			if num.isdigit():
				num = int(num)
				if 1 <= num <= len(liste):
					print(f"Article '{liste[num-1]}' supprimé !")
					del liste[num-1]
				else:
					print("Numéro invalide.")
			else:
				print("Entrée non valide.")
		elif choix == "5":
			sauvegarder_liste(liste)
			print("Liste sauvegardée. Au revoir !")
			break
		else:
			print("Choix invalide.")

# Point d'entrée du programme
if __name__ == "__main__":
	main()
