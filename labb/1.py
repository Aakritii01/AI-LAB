import random

def get_user_guess():
    return int(input("Guess a number between 1 and 100: "))

def check_guess(guess, secret):
    if guess < secret:
        print("Too low!")
        return False
    elif guess > secret:
        print("Too high!")
        return False
    else:
        print("Correct! You guessed it!")
        return True

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")

    while not guessed:
        guess = get_user_guess()
        attempts += 1
        guessed = check_guess(guess, secret_number)

    print(f"You took {attempts} attempts.")

# Start the game
play_game()