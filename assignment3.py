import random 

secret_number = random.randint(1, 100)
print("Number Guessing Game!")
print("Thinking of a number between 1 and 100...")

while True: 
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number")
        continue

    guess = int(guess)
    if guess < secret_number:
        print("T00 Low, Try again hahaha")
    elif guess > secret_number:
        print("Too high lil bro, try again")

    else:
        print(" You guesses the right number, finally!")
        break