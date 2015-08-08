
HIDDEN_NUMBER = 3

def start_game():

    number_of_guesses = 0
    while number_of_guesses < 3:
        guess_string = input('Guess a number between 1 and 10: ')
        guess = int(guess_string)

        # validate user input
        if 1 <= guess <= 10:
            if guess == HIDDEN_NUMBER:
                print('Congrats! You got it right.')
                break
            else:
                print("That's wrong.")
                number_of_guesses += 1
        else:
            print('I said, a number between 1 and 10!!!')


if __name__ == '__main__':
    start_game()
