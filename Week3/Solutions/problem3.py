# -*- coding: utf-8 -*-


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = string.ascii_lowercase
    HaHa = ''
    for x in secretWord:
        if x not in lettersGuessed:
          HaHa += x
    return HaHa

getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))