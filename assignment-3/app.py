#----Deductive logic game - guess the secret number
import random


# 🎯 Generate a random 3-digit secret number (as a string for easy comparison)
secret_number = str(random.randint(100,999))

# 🔄 Player has 10 attempts
attempts = 10

print("🎮 Welcome to the Deductive Logic Game!")
print("Try to guess the 3-digit secret number.")
print("Hints: 👌 = Correct Place | 👍 = Wrong Place | ❌ = No Correct Digit")
print("-" * 50)

# 🚀 Game Loop

for attempt in range (1, attempts+1):
    guess= input(f"Attempt {attempt}/{attempts} - Enter a 3-digit number:")

    # 🛑 Input validation (Must be exactly 3 digits)
    if len(guess) != 3 or not guess.isdigit():
        print("Please enter a valid 3-digit number!\n")
        continue

    # ✅ Check if the guess is correct
    if guess == secret_number:
        print("🎉👌👌👌 Congratulations! YOU GOT IT")
        break

    # 🧩 Give Hints
    feedback = []
    for i in range(3):
        if guess[i] == secret_number[i]:
            feedback.append("👌") # Correct digit in the correct place
        elif guess[i] in secret_number:
            feedback.append("👍") # Correct digit but in the wrong place
        else:
            feedback.append("❌") # Incorrect digit

    # 🔁 Display Feedback
    print(" ".join(feedback), "\n")    

else:
    print(f"❌ Game over! The secret number was {secret_number}. Better luck next time!")





