from __future__ import division, print_function, unicode_literals
input = raw_input

hidden_word = 'tiger'
true_letters = set(hidden_word)

def start_game():
    running = True

    while running:

        guess = input('> ')

        if guess.lower() == 'q':
            print("Quitting...")
            break

        if len(guess) != 5:
            print("I need a five-letter word")
            continue

        response = []
        for letter, true_letter in zip(guess, hidden_word):
            if letter == true_letter:
                response.append('[' + letter + ']')
            elif letter in true_letters:
                response.append('(' + letter + ')')
            else:
                response.append(letter)
        
        print(''.join(response))






