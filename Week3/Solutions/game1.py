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
    return all(letters in ''.join(lettersGuessed) for letters in secretWord)

def letterInWord(guess, secretWord):
    '''
    guess: user input, the letter that they guessed
    secretWord: string, the word the user is guessing
    returns: boolean, True if a letter is in the word; False otherwise
    '''
    gotOne = False
    
    if guess in secretWord:
        gotOne = True
    else:
        gotOne = False
        
    return gotOne

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    currentGuess=''
    
    for letter in secretWord:
        
        if letter in lettersGuessed:
            currentGuess += letter
            
        else:
            currentGuess += ' _ '
    
    return currentGuess

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''    
    alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for letter in lettersGuessed:
        
        if letter in alphabet:
            alphabet.remove(letter)
        else:
            break
            
    return ''.join(alphabet)


