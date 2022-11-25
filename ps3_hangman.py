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
secretWord = chooseWord(wordlist).lower()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    prWord = ''
    for w in secretWord:
        if w in lettersGuessed:
            prWord = prWord + w
        else:
            prWord = prWord + ' _'
    return prWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    
    letters_avail = [ch for ch in string.ascii_lowercase if ch not in lettersGuessed]
    
    return ''.join(letters_avail)

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
    import string
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord))
      + " letters long.")
    
    #  The letters that have been guessed so far
    lettersGuessed = []
    #The number of incorrect guesses made so far
    mistakesMade = 0
    #The number of the trials an user can make
    numberOfTry = 8
    #The Flag variable. True if guessed. False not guessed yet.
    guessedFlag = False
    #The letters that may still be guessed
    availableLetters = string.ascii_lowercase
    
    while mistakesMade < numberOfTry and not guessedFlag:
        print("-------------")
        print("You have " + str(numberOfTry-mistakesMade) 
              + " guesses left.")
        print("Available letters: " + availableLetters)
        inpLetter = input("Please guess a letter: ").lower()
        lettersGuessed.append(inpLetter)
        
        if inpLetter not in availableLetters:
            print("Oops! You've already guessed that letter: "
                  + getGuessedWord(secretWord, lettersGuessed)) 
        elif inpLetter in secretWord:
            print("Good guess: " 
                  + getGuessedWord(secretWord, lettersGuessed))
            guessedFlag = isWordGuessed(secretWord, lettersGuessed)
        else:
            mistakesMade += 1
            print("Oops! That letter is not in my word: " 
                  + getGuessedWord(secretWord, lettersGuessed))
        availableLetters = getAvailableLetters(lettersGuessed)
    
    print("-------------")
    if guessedFlag:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was "
              + secretWord + ".")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
