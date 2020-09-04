# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
    status = True
    
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed: #Just check if each letter of the secret word is inside the list
            status = False
            
    return status

#print(isWordGuessed("apple", ['e','i','k','p','r','s','a','l']))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    attempt = ""
    
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            attempt += secretWord[i]
        else:
            attempt += "_ "
            
    return attempt

#print(getGuessedWord("apple", ['e','i','k','p','r','s']))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in alphabet:
            alphabet = alphabet.replace(lettersGuessed[i], '')
    
    return alphabet
            
#print(getAvailableLetters(['a','z','erfv','o','w','f']))

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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    print('----------')
    
    mistakesMade = 0
    lettersGuessed = []
    
    while mistakesMade < 8: #End the game after 8 mistakes
        
        print('You have', 8-mistakesMade, 'guesses left')
        availableLetters = getAvailableLetters(lettersGuessed) #Remaining letters
        print('Available letters:', availableLetters)
        
        guess = input("Please guess a letter: ") #Ask for a letter
        guessLetter = guess.lower() #Lower case
        if guessLetter not in availableLetters: #Not a mistake, just to prevent bug or repetition
            print('Oops, you\'ve already guessed that letter, or it is not possible:', getGuessedWord(secretWord, lettersGuessed))
        elif guessLetter not in secretWord: #An actual mistake
            print('Oops, that letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            mistakesMade += 1
            lettersGuessed.append(guessLetter)
        else: #The letter was correct
            lettersGuessed.append(guessLetter)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        
        print('----------')
        if isWordGuessed(secretWord, lettersGuessed): #Exit game if the word is fully guessed
            print('Congratulations, you won!')
            return True
        
    print("Sorry, you ran out of guesses, the word was " + secretWord + ".")
    return False 



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
