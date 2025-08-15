import random

# Welcome message and game explanation
print("🎯 Welcome to the Number Guessing Game! 🎯")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it? You have 10 attempts!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

# Main game loop
while attempts < max_attempts:
    # Get player's guess
    try:
        guess = int(input(f"\nEnter your guess (attempt {attempts + 1}/{max_attempts}): "))
        attempts += 1
        
        # Check if guess is valid
        if guess < 1 or guess > 100:
            print("❌ Please enter a number between 1 and 100!")
            attempts -= 1  # Don't count invalid guesses
            continue
        
        # Check if guess is correct
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            print(f"The number was {secret_number}")
            break
        elif guess < secret_number:
            print("📈 Too low! Try a higher number.")
        else:
            print("📉 Too high! Try a lower number.")
        
        # Show remaining attempts
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
    
    except ValueError:
        print("❌ Please enter a valid number!")
        attempts -= 1  # Don't count invalid inputs
        continue

# Game over message
if attempts >= max_attempts and guess != secret_number:
    print(f"\n😔 Game Over! You ran out of attempts.")
    print(f"The number was {secret_number}")

print("\nThanks for playing! 👋")
