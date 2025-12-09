# Basic Math Quiz Game
import random
# Step 1: Define the math questions function
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return f"What is {num1} {operation} {num2} ?", answer  

# Step 2: Main Quiz Game function
def math_quiz():
    score = 0
    rounds = 5
    
    print("\n=== Welcome to the Math Quiz! ===\n")
    print("You will be asked 5 questions. Try to answer them correctly!\n")

    for _ in range(rounds):
        question, correct_answer = generate_question()
        print(f"\nQuestion {_ + 1}: {question}")
        user_answer = int(input("Your answer: "))
        
        if user_answer == correct_answer:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    
    print("\n=== Quiz Over! ===")
    print(f"\nYour final score is: {score}/{rounds}.")
    if score == rounds:
        print("Excellent work! You nailed it! 🏆")
    elif score >= rounds // 2:
        print("Good job! Keep practicing! 👍")
    else:
        print("Don't worry, practice makes perfect! 💪")

# Step 3: Run the Game
math_quiz()