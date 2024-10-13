import random

def func():
      user_selection = input("Enter a choice (rock, paper, scissors): ")
      options = ["rock", "paper", "scissors" ]
      computer_selection = random.choice(options)
      print("You chose : ", user_selection, "\ncomputer chose : ",computer_selection)
      if user_selection == computer_selection:
         print("Both players selected", user_selection , "It's a tie!")
      elif user_selection == "rock":
         if computer_selection == "scissors":
           print("Rock smashes scissors! You win!")
         else:
           print("Paper covers rock! You lose.")
      elif user_selection == "paper"  :
         if computer_selection == "rock":
          print("Paper covers rock! You win!")
         else:
          print("Scissors cuts paper! You lose.")
      elif user_selection == "scissors":
         if computer_selection == "paper"  :
            print("Scissors cuts paper! You win!")
         else:
          print("Rock smashes scissors! You lose.")


func()
user=input("Do you want to play again?")
if user == "yes" or user == "Yes":
   func()
else:
   print("Have a good day")