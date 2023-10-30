import random
import string

print("HANGMAN: THE GAME")

wordbank = [
    "howard",
    "bison",
    "fruits",
    "trinidad",
    "python",
    "programs",
    "straw",
    "fox",
    "zebra",
    "blueberry",
    "cattle",
]
gameWord = random.choice(wordbank).lower()
wordGuessed = list("_" * len(gameWord))


def hangman_structure(wrongGuess):
    if wrongGuess == 0:
        print("\n_________")
        print("|         |")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("--------   ")
    elif wrongGuess == 1:
        print("\n_________")
        print("|         |")
        print("|         0")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("--------   ")
    elif wrongGuess == 2:
        print("\n_________")
        print("|         |")
        print("|         O")
        print("|         |")
        print("|         |")
        print("|          ")
        print("|          ")
        print("--------   ")
    elif wrongGuess == 3:
        print("\n_________")
        print("|         |")
        print("|         O")
        print("|        /|")
        print("|         |")
        print("|          ")
        print("|          ")
        print("--------   ")
    elif wrongGuess == 4:
        print("\n_________")
        print("|         |")
        print("|         O")
        print("|        /|\\")
        print("|         |")
        print("|          ")
        print("|          ")
        print("--------   ")
    elif wrongGuess == 5:
        print("\n_________")
        print("|         |")
        print("|         O")
        print("|        /|\\")
        print("|         |")
        print("|       _/ ")
        print("|          ")
        print("--------   ")
    elif wrongGuess == 6:
        print("\n_________")
        print("|         |")
        print("|         O")
        print("|        /|\\")
        print("|         |")
        print("|       _/ \\")
        print("|          ")
        print("--------   ")


def printGuess(lettersGuessed):
    result = ""
    for i in range(len(gameWord)):
        if gameWord[i] in lettersGuessed:
            result += gameWord[i] + " "
        else:
            result += wordGuessed[i] + " "
    return result


stillPlaying = True
wrongGuesses = 0
maxWrongGuesses = 6
letters_guessed = []

while stillPlaying:
    guess = None

    print("\n" + printGuess(letters_guessed))

    guess = input("Guess a letter or guess the whole word: ").lower()

    if len(guess) == 1:
        if guess in letters_guessed:
            print("You've already guessed that letter.")
        elif guess in gameWord:
            print(guess, "is in the word")
            letters_guessed.append(guess)
            for i in range(len(gameWord)):
                if gameWord[i] == guess:
                    wordGuessed[i] = guess
            if "".join(wordGuessed) == gameWord:
                print(f"Congratulations! You've guessed the word: {gameWord}.")
                stillPlaying = False
        else:
            print("Incorrect guess. Try Again!")
            letters_guessed.append(guess)
            wrongGuesses += 1
            if wrongGuesses >= maxWrongGuesses:
                print(hangman_structure(wrongGuesses))
                print("You ran out of chances. The word was:", gameWord)
                stillPlaying = False
            else:
                print(hangman_structure(wrongGuesses))
    else:
        if guess == gameWord:
            print(f"Congratulations! You've guessed the word: {gameWord}.")
            stillPlaying = False
        else:
            print("Incorrect guess.")
            wrongGuesses += 1
            if wrongGuesses >= maxWrongGuesses:
                print(hangman_structure(wrongGuesses))
                print("You ran out of chances. The word was:", gameWord)
                stillPlaying = False

if not stillPlaying:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        # Reset the game if the player wants to play again
        gameWord = random.choice(wordbank).lower()
        wordGuessed = list("_" * len(gameWord))
        stillPlaying = True
        wrongGuesses = 0
        letters_guessed = []
