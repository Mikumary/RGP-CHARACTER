import random
def get_chioces():
  player_choice = input("Enter a choice(rock, paper, scissors:)")
  options = ["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice,"computer": computer_choice}
  if player_choice not in options:
   print("invalid input")

  return choices

def check_win(player,computer):
 print(f"You chose {player} and computer chose {computer}")
 if player == computer:
  return "it's a tie!"
 elif player == "rock":
   if computer == "scissors":
    return "Rock smashes scissors! You win."
   else:
    return "paper covers rock! You lose"
 elif player == "paper":
   if computer == "rock":
    return "Paper covers rock! You win."
   else:
    return "Scissors cuts paper! You lose"  
 elif player == "scisors":
   if computer == "paper":
    return "Scissors cuts paper! You win."
   else:
    return "Rock smashes scissors! You lose"  
while True:
 get_chioces()
 

Choices= get_chioces()
result= check_win(Choices["player"], Choices["computer"])
print(result)