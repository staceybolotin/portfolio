rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = '''
Lizard
    _______________
---'     __________)
        /
       |
        \_______
        ________)
______'
'''

spock = '''
Spock
    _______
---'   ____)____
          ______)
          _______)
         |______
         _______)
---.__________)
'''

#Write your code below this line 👇
import random

answers = [rock, paper, scissors, lizard,
           spock], ["rock", "paper", "scissors", "lizard", "spock"]

computer_choice = random.randint(0, 4)
computer_choice_str = answers[1][computer_choice]
#print(answers[1][computer_choice])

print("Welcome to the Rock, Paper, Scissors, Lizard, Spock game!")
player = (input("Please make the choice and let the best player win! ")).lower()

if answers[1].count(player) == 0:
  print("You lose! Rules are important! Muahahaha! Skynet is out to get you.")
else:
    #print human's and computer's choices
    print("\nYOU CHOSE:")
    print(answers[0][answers[1].index(player)])
    print("\nCOMPUTER CHOSE:")
    print(answers[0][computer_choice])


    #if player and computer choose the same thing
    if answers[1].index(player) == computer_choice:
        print("It's a tie! Great minds think alike.")
    #player chose ROCK
    elif player == "rock":
      if computer_choice_str == "paper":
        print("You lose! Paper covers rock!")
      elif computer_choice_str == "scissors":
        print("You win! Rock crushes scissors!")
      elif computer_choice_str == "lizard":
        print("You win! Rock crushes lizard!")
      elif computer_choice_str == "spock":
        print("You lose! Spock vaporizes rock!")
    #player chose PAPER
    elif player == "paper":
        if computer_choice_str == "rock":
            print("You win! Paper covers rock!")
        elif computer_choice_str == "scissors":
            print("You lose! Scissors cut paper!")
        elif computer_choice_str == "lizard":
            print("You lose! Lizard eats paper!")
        elif computer_choice_str == "spock":
            print("You win! Paper disproves Spock!")
    #player chose SCISSORS
    elif player == "scissors":
        if computer_choice_str == "rock":
            print("You lose! Rock crushes scissors!")
        elif computer_choice_str == "paper":
            print("You win! Scissors cut paper!")
        elif computer_choice_str == "lizard":
            print("You win! Scissors decapitate lizard!")
        elif computer_choice_str == "spock":
            print("You lose! Spock smashes scissors!")
    #player chose LIZARD
    elif player == "lizard":
        if computer_choice_str == "rock":
            print("You lose! Rock crushes lizard!")
        elif computer_choice_str == "paper":
            print("You win! Lizard eats paper!")
        elif computer_choice_str == "scissors":
            print("You lose! Scissors decapitate lizard!")
        elif computer_choice_str == "spock":
            print("You win! Lizard poisons Spock!")
    #player chose SPOCK
    elif player == "spock":
        if computer_choice_str == "rock":
            print("You win! Spock vaporizes rock!")
        elif computer_choice_str == "paper":
            print("You lose! Paper disproves Spock!")
        elif computer_choice_str == "lizard":
            print("You lose! Lizard poisons Spock!")
        elif computer_choice_str == "scissors":
            print("You win! Spock smashes scissors!")

