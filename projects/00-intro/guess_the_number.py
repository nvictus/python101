
HIDDEN_NUMBER = 3

def start_game_forloop():

    for i in range(3):
        guess = input('Guess a number between 1 and 10: ')
        guess_number = int(guess)

        # validate user input
        if 1 <= guess_number <= 10:
            if guess_number == HIDDEN_NUMBER:
                print('Congrats! You got it right.')
                break
            else:
                print("That's wrong.")
        else:
            print('I said, a number between 1 and 10!!!')






start_game_forloop()
