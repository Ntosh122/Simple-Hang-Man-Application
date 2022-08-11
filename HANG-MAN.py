import random


def HangMan():
    # print wordlist
    with open('words.txt', 'r') as file:
        for x in file:
            for line in x.split():
                print(line, end=" ")
        print("\n")
    with open('words.txt', 'r') as f:
        words = f.readlines()
    word = random.choice(words)[:-1]
    allowed_errors = 7
    guesses = []
    done = False

    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
        done = True

        guess = input(f'Allowed Errors left {allowed_errors}, Next Guess: ')
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            allowed_errors -= 1
            if allowed_errors == 0:
                break
        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False
    if done:
        print(f'Congratulations!!!!!!, You have found the word, it was {word}')
    else:
        print(f'Game Over, the word was {word}')


HangMan()
