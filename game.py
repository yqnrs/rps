import random

rps = ['rock', 'paper', 'scissors']

def ai(rps):
  choice = (random.choice(rps)) 
  print("Ai played...", choice)
  return choice
  
while True: 
  human = input("Enter Your Choice:")
  valid_choices = ["rock", "paper", "scissors"]
  if human == 'leave':
    break
  if (human.lower()) not in valid_choices:
    print("That isn't a choice")
    continue 

  aic = ai(rps)

  if aic == 'rock' and human == 'paper':
        print("You Win!")
  if aic == 'rock' and human == 'scissors':
        print("You Lose!")
  if aic == 'paper' and human == 'rock':
        print("You Lose!")
  if aic == 'paper' and human == 'scissors':
        print("You Win!")
  if aic == 'rock' and human == aic:
        print("You tie!")
  if aic == 'paper' and human == aic:
        print("You tie!")
  if aic == 'scissors' and human == 'rock':
        print("You Win!")
  if aic == 'scissors' and human == 'paper':
        print("You Lose!")
  if aic =='scissors' and human == aic:
        print("You tie!")

play_again = input("Play Again? (yes/no): ")
if play_again.lower() != "yes": 
  break
