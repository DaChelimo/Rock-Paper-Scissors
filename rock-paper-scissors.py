from random import randint

print("Welcome to rock, paper, scissors \n")

computer_choice = ["rock", "paper", "scissors", "rock", "paper", "scissors"]
new = "\n"

points = 0
coins = 0

player = input().lower()
computer = computer_choice[randint(0, 6)]
r = "rock"
p = "paper"
s = "scissors"

print("Round 1: \n")
print("You chose:", player)
print("Computer chose:", computer, )

if player == computer:
    print("Tie")
elif player == r and computer == s:
    print("You won Round 1")
    points += 1
elif player == r and computer == p:
    print("Computer won Round 1")
    coins += 1
elif player == p and computer == s:
    print("Computer won Round 1")
    coins += 1
elif player == p and computer == r:
    print("You won Round 1")
    points += 1
elif player == s and computer == r:
    print("Computer won Round 1")
    coins += 1
elif player == s and computer == p:
    print("You won Round 1")
    points += 1

print(new)

player = input().lower()
computer = computer_choice[randint(0, 6)]

print("Round 2: \n")
print("You chose:", player)
print("Computer chose:", computer, )

if player == computer:
    print("Tie")
elif player == r and computer == s:
    print("You won Round 2")
    points += 1
elif player == r and computer == p:
    print("Computer won Round 2")
    coins += 1
elif player == p and computer == s:
    print("Computer won Round 2")
    coins += 1
elif player == p and computer == r:
    print("You won Round 2")
    points += 1
elif player == s and computer == r:
    print("Computer won Round 2")
elif player == s and computer == p:
    print("You won Round 2")
    points += 1

print(new)

player = input().lower()
computer = computer_choice[randint(0, 6)]

print("Round 3: \n")
print("You chose:", player)
print("Computer chose:", computer)

if player == computer:
    print("Tie")
elif player == r and computer == s:
    print("You won Round 3")
    points += 1
elif player == r and computer == p:
    print("Computer won Round 3")
    coins += 1
elif player == p and computer == s:
    print("Computer won Round 3")
    coins += 1
elif player == p and computer == r:
    print("You won Round 3")
    points += 1
elif player == s and computer == r:
    print("Computer won Round 3")
    coins += 1
elif player == s and computer == p:
    print("You won Round 3")
    points += 1

print(new)
if points > coins:
    print("You won the game")
elif points == coins:
    print("It's a draw")
elif points < coins:
    print("Computer won the game")
