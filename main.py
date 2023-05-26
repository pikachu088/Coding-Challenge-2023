#!usr/bin/env python

#syafiqah, hana
import random

def main():
    """Start a music guessing game."""
    print("Guess the music!")
# mengisytiharkan 
    song = [
      "enchanted",
      "blank space",
      "love story",
      "you belong with me",
      "lover",
      "cardigan",
      "back to desember"
      ]

    x = random.choice(song)
    
    guess = None
# memulakan gelung game
    while x != guess:

        guess = str(input("what song am I thinkin of?"))

        if x == guess:
            print("You guessed {}. Congratulation you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again! put another taylor swift song.format(guess")

main()