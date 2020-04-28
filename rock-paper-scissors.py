from random import randint

print("Welcome to rock, paper, scissors \n")

computer_choice = ["rock", "paper", "scissors", "rock", "paper", "scissors"]
new = "\n"

player = input().lower()
computer = computer_choice[randint(0, 5)]
r = "rock"
p = "paper"
s = "scissors"

print("Round 1: \n")
print("You chose:", player)
print("Computer chose:", computer, )

if player == computer:
    print("Tie")
elif player == r and computer == s:
    print("You won")
elif player == r and computer == p:
    print("Computer won")
elif player == p and computer == s:
    print("Computer won")
elif player == p and computer == r:
    print("You won")
elif player == s and computer == r:
    print("Computer won")
elif player == s and computer == p:
    print("You won")

print(new)

player = input().lower()
computer = computer_choice[randint(0, 5)]

print("Round 2: \n")
print("You chose:", player)
print("Computer chose:", computer, )

if player == computer:
    print("Tie")
elif player == r and computer == s:
    print("You won")
elif player == r and computer == p:
    print("Computer won")
elif player == p and computer == s:
    print("Computer won")
elif player == p and computer == r:
    print("You won")
elif player == s and computer == r:
    print("Computer won")
elif player == s and computer == p:
    print("You won")

print(new)

player = input().lower()
computer = computer_choice[randint(0, 5)]

print("Round 2: \n")
print("You chose:", player)
print("Computer chose:", computer, )

if player == computer:
    print("Tie")
elif player == r and computer == s:
    print("You won")
elif player == r and computer == p:
    print("Computer won")
elif player == p and computer == s:
    print("Computer won")
elif player == p and computer == r:
    print("You won")
elif player == s and computer == r:
    print("Computer won")
elif player == s and computer == p:
    print("You won")