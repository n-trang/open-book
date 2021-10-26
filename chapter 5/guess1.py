import random

def guess_game(low, high):
    number = random.randrange(low, high)
    my_guess = int(input("My guess between"))
    number_of_guesses = 1
    while my_guess != number:
        if my_guess > number:
            print(my_guess, "is too high")

        elif my_guess < number:
            print(my_guess, "is too low")
        my_guess = int(input("guess again: "))
        number_of_guesses += 1

    print("congrats, you guessed it right after", number_of_guesses, "guesses.")

guess_game(0, 10)
