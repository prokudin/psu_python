# -*- coding: utf-8 -*-

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True
