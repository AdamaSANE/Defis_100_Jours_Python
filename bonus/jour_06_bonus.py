
# Bonus Jour 6 : Quiz mathématique avec division et minuteur
import random
import time

def poser_question(a, b, op):
	if op == '/':
		a = a * b
		question = f"{a} / {b} = ? (entier)"
		reponse_attendue = a // b
	elif op == '+':
		question = f"{a} + {b} = ?"
		reponse_attendue = a + b
	elif op == '-':
		question = f"{a} - {b} = ?"
		reponse_attendue = a - b
	else:
		question = f"{a} * {b} = ?"
		reponse_attendue = a * b
	return question, reponse_attendue

def quiz():
	print("Bienvenue au défi bonus du Jour 6 ! 🧮")
	nb_questions = int(input("Combien de questions voulez-vous jouer ? "))
	temps_limite = float(input("Temps limite par question (en secondes, ex: 5) : "))
	score = 0
	operations = ['+', '-', '*', '/']
	for tour in range(1, nb_questions + 1):
		op = random.choice(operations)
		a = random.randint(1, 10)
		b = random.randint(1, 10)
		question, reponse_attendue = poser_question(a, b, op)
		print(f"\nQuestion {tour}/{nb_questions} : {question}")
		debut = time.time()
		reponse = input(f"Votre réponse (vous avez {temps_limite} secondes) : ")
		duree = time.time() - debut
		if duree > temps_limite:
			print("⏰ Temps écoulé !")
		elif reponse.strip() == str(reponse_attendue):
			print("✅ Bonne réponse !")
			score += 1
		else:
			print(f"❌ Mauvaise réponse. La bonne réponse était {reponse_attendue}")
	print(f"\nQuiz terminé ! Votre score : {score}/{nb_questions}")

if __name__ == "__main__":
	quiz()
