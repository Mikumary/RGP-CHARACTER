"""Write a program that does the following:

The computer picks a secret number between 1 and 10.

The user has to guess the number.

If the guess is correct → print "You got it!"

If the guess is too low → print "Too low!"

If the guess is too high → print "Too high!"

Keep asking until the user guesses correctly."""

import random
secret = random.randint(1,100)
while True:
  guess=input("guess any number: ")
  if guess.lower()=="quit":
      print ("goodbye thank you for trying")
      print (f"the answer was {secret}")
      break
  try:
    guess=int(guess)
  except ValueError:
     print("please enter a digit or type quit")
     continue
  if guess==secret:
        print("you got it")
  elif guess<secret:
        print("The number is too low")
  elif guess>secret:
        print("the number is to high")
  elif abs(secret - guess) <=5:
      print ("you are very close")
