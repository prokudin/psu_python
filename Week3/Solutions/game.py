#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 08:47:34 2019

@author: avp5627
"""

import random

def load_words():
    """
    loads words from the file
    """
    with open('words_alpha.txt') as word_file:
        valid_words = word_file.read().split()

    return valid_words

words = load_words()

def chooseWord(wordlist):
    """
    chooses random word
    """
    return random.choice(wordlist)

secret = chooseWord(words)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = False
    for letter in lettersGuessed:
        if letter in secretWord:
            result = True
        else: 
            result = False
    return result  

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord=''
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessedWord += "_ "
        else:
            guessedWord += letter

    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    availableLetter=''
    
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetter += letter
    
    return availableLetter

