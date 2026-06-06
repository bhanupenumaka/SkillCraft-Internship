import random

def guess_game():
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100!")
    
    while True:
        try:
            user_guess = int(input("Your guess: "))
            if user_guess < number:
                print("Too low!")
            elif user_guess > number:
                print("Too high!")
            else:
                print("Correct! You win!")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_game()
