from random import choice
import art
import game_data

def compare_generator():
    """
    Generate the first person to be compared and removes it from the data
    so it will not be picked again
    """
    random_compare = choice(game_data.data)
    game_data.data.remove(random_compare)

    return random_compare


def against_generator():
    """
    Generate the second person to be compared and removes it from the data
    so it will not be picked again
    """
    random_against = choice(game_data.data)
    game_data.data.remove(random_against)

    return random_against


def check_most_follower():

    """
    Checks who have the most followers
    :return: That one with most followers
    """

    if compare['follower_count'] > against["follower_count"]:
        return compare["follower_count"]

    elif compare['follower_count'] < against["follower_count"]:
        return against["follower_count"]



def guess_checker(user_guess):
    """
    Takes the letter that the user guessed and turns it into a variable to be used on guess_follower_function
    :param user_guess:
    :return:
    """
    if user_guess == 'A':
        user_choice = compare
        return user_choice

    elif user_guess == 'B':
        user_choice = against
        return user_choice

    else: # alert the user in case it miss typed, but the program ends anyway...
            print("\nPlease try again, you've miss typed")


### Game starts here ###
compare = compare_generator()
score = 0
game_is_over = False
print(art.logo)

while game_is_over is False:

    against = against_generator() #always generate the second line to be guessed

    print(f"Compare A: {compare['name']}, {compare['description']}, {compare['country']}")
    print(art.vs)
    print(f"Against B: {against['name']}, {against['description']}, {against['country']}")

    guess = input("Who has more followers ? Type 'A' or 'B': ").upper()

    #check if the user guessed right, and if it did, than maintain the correct guess in the game
    if guess_checker(guess)['follower_count'] == check_most_follower():
        compare = guess_checker(guess) # maintain the correct guess in the game in the first line to be compared
        score += 1 #add 1 point to the score
        print("\n" * 30) #clear the console
        print(art.logo)
        print(f"You're right! Current score: {score}")

    # but if the user guess is wrong, then the game stops
    else:
        print(f"\nSorry, that's wrong. Final score: {score}")
        game_is_over = True

    #checks how many more persons are on the game data e ends the program once the player guessed everyone correctly
    if len(game_data.data) == 0:
        print("Congratulations, you finished the game with the highest score")
        print(f"Final Score: {score}")
        game_is_over = True
