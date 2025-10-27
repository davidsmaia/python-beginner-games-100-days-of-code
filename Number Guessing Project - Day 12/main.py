# TODO - Import the logo to the game
# TODO - Make the computer select a number between 1 and 100
# TODO - Change the attempts by 10 for easy and by 5 for hard
# TODO - Identify if my guess was higher or lower then the selected number
# TODO - Create a loop to make the game continuing until I guess corectly
# TODO - Now, reduce my attempts by every mistake I made and stops when it's 0...

import random

import art

def select_difficulty():
    global attempts
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts += 5

    return attempts

attempts = 5
print(art.logo)

print("Welcome to the Number Guessing Game! \n"
      "I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
select_difficulty()

while attempts > 0:

    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    attempts -= 1

    if attempts == 0:
        print(f"\nYou've run out of guesses. The correct answer is {number}\n"
              f"Refresh the page to run again")

    else:
        if guess == number:
            print(f"\nYou got it, the answer was {number}")
            game_is_over = True

        elif guess < number:
            print("\nToo low \nGuess again")

        else:
            print("\nToo high \nGuess again")
