#%%

import random
from milestone_2.py import word_list

## create class
## num_lives: int - The number of lives the player has at the start of the game.
## word_list: list - A list of words

class Hangman
   def __init__ (self, word_list, num_lives = 5):
     self.word_list = word_list
     self.num_lives = num_lives
     return

## word: The word to be guessed, picked randomly from the word_list.
   def word (self, word):
     self.word = word
     return
word()

## word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']   
   def word_guessed (self, word_guessed):
     self.word_guessed = ['_']
       if guess in word:
       print (guess)
       break
       if guess not in word:
       print ('_')
     return
word_guessed()

 ## num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet   
    def num_letters (self, num_letters):
      self.num_letters = num_letters
      return
num_letters()

## list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially      
    def list_of_guesses (self, list_of_guesses = []):
      self.list_of_guesses = list_of_guesses   
      return
list_of_guesses()

## create methods for running checks

def check_guess ()
    guess.lower()
    if guess in word
      print ("Good guess! {guess} is in the word.")
    for letter in guess
      if letter == word_guessed
      print (word_guessed.replace (['_'], guess))
    for num_letters.append -=1
     print ('You have {num_letters} remaining')
    else num_lives.append -= 1
     print ("Sorry, {letter} is not in the word.")
     print ("You have {num_lives} lives left.")
    return

check_guess()

def ask_for_input (self, ask_for_input)
   while True:
    guess = input()
     if guess.isalpha() =!
        print ("Invalid letter. Please, enter a single alphabetical character.")
     elif guess in list_of_guesses:
        print ("You already tried that letter!")
        break
    else check_guess(guess)
        list_of_guesses.append(guess)
    return

ask_for_input()

def play_game (word_list):
   num_lives = [5]
   game = Hangman.get()
   game = (word_list, num_lives)
   while True:
    if num_lives ==0:
    print ("Game over, you lost!")
    break
    if num_letters >0:
    ask_for_input()
    elif num_lives =! 0 and num_letters ==0:
    print ("Congratulations. You won the game!")
    return

play_game(word_list)
