# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    letterstemp = [x for x in secretWord if x in lettersGuessed]
    letterstemp = ''.join(letterstemp)
    if letterstemp == secretWord:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter, '- ')
        else:
            pass
    return secretWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lowerletter = 'abcdefghijklmnopqrstuvwxyz'
    for letter in lettersGuessed:
        lowerletter = lowerletter.replace(letter, '')
    return lowerletter


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    mistakesMade = 0
    lettersGuessed = []
    print("I am thinking of a word that is " +
          str(len(secretWord)) + " letters long.")
    while (mistakesMade != 8):
        flag = 1
        print('-----------------------------------------------------')
        print("You have " + str(8 - mistakesMade) + " guesses left.")
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available letters: " + availableLetters)
        userGuessed = input("Please guess a letter: ")
        if (userGuessed in lettersGuessed):
            print("Oops! You've already guessed that letter: ", end="")
            flag = 0
        lettersGuessed.append(userGuessed)
        stepletter = getGuessedWord(secretWord, lettersGuessed)
        if (flag == 0):
            print(stepletter)
        if (userGuessed in secretWord) and (flag == 1):
            print("Good guess: " + stepletter)
        elif flag == 1:
            print("Oops! That letter is not in my word: " + stepletter)
            mistakesMade += 1
        if isWordGuessed(secretWord, lettersGuessed):
            print('-----------------------------------------------------')
            print('Congratulations, you won!')
            break
    if(mistakesMade == 8):
        print('-----------------------------------------------------')
        print("Sorry, you ran out of guesses. The word was: " + secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
