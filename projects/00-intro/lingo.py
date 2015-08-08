HIDDEN_WORD = 'tiger'
letters = set(HIDDEN_WORD)


def start_game():
    """
    LINGO!
    ======

    Guess the hidden five-letter word!
    - If a letter and its position are correct, it will be delimited by `[]`
    - If the position is incorrect but the letter occurs in the word, it will be 
      delimited by `()`

    Enter Q to quit.

    """
    print(start_game.__doc__)

    while True:

        guess = input('> ')

        if guess.lower() == 'q':
            print("Quitting...")
            break

        if len(guess) != 5:
            print("I need a five-letter word")
            continue

        response = []
        for guess_letter, target_letter in zip(guess, HIDDEN_WORD):
            if guess_letter == target_letter:
                response.append('[' + guess_letter + ']')
            elif guess_letter in letters:
                response.append('(' + guess_letter + ')')
            else:
                response.append(guess_letter)
        
        print(''.join(response))

        if guess == HIDDEN_WORD:
            print("Congrats!")
            break


if __name__ == '__main__':
    start_game()

