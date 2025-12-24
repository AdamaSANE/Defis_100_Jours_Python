# Random Password Generator
import random, string

#step 1: Define Password Generator Function
def generate_password(length=12):
    """Generate a random password containing letters, digits, and punctuation."""
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Define character sets for password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all sets
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

# Step 2: User Interaction
try:
    user_length = int(input("Enter desired password length (minimum 4): "))
    password = generate_password(user_length)
    print(f"Generated Password: {password}")
except ValueError as e:
    print(f"Error: {e}")
    