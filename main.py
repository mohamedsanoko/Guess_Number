import random

def giving_directions(user_guess, random_number):
  if user_guess > random_number:
    print("Too high.")
  else: 
    print("Too low.")
#Generate a random number between 1 and a 100
print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
#Prompt the user to choose between the easy game or the hard game
user_decision = input("Choose a difficulty. Type 'easy' or 'hard': ")
#Set up a loop for the easy and the hard game, the loops should have 5 and 10 iterations respectively
if user_decision == "easy":
  count = 10
  for i in range(0, 10):
    print(f"You have {count} attempts remaining to guess the number.")
    count = count - 1
    user_guess = int(input("Make a guess: "))
    if user_guess == random_number:
      break
    else:
      giving_directions(user_guess, random_number)
elif user_decision ==  "hard":
  count = 5
  for i in range(0, 5):
    print(f"You have {count} attempts remaining to guess the number.")
    count = count - 1
    user_guess = int(input("Make a guess: "))
    if user_guess == random_number:
      break
    else:
      giving_directions(user_guess, random_number)

if count == 0:
  print("You used all of your guesses. You lost.")
  print(f"The number was {random_number}.")
else:
  print(f"Congratulations you managed to guess the number {random_number}, you win!")
#In each iteration prompt the user to enter a number
#Check if the number the user entered correspond to the actual number, if it does break out of the loop and announce to the user that he won the game
#Use this number as input to a function you will create that will tell the user if he guessed too high or if he guessed too low
#Keep a counter that will be able to tell you at the end of the loop whether the user managed to guess it or not which will allow you to declare him as winner or loser

