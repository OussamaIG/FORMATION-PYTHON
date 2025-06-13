print("Options are: Rock, Paper, Scissors")

p1 = input("Player 1, enter your choice: ").strip().lower()
p2 = input("Player 2, enter your choice: ").strip().lower()


if p1 == p2:
    print("It's a tie!")

elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "paper" and p2 == "rock") or \
     (p1 == "scissors" and p2 == "paper"):
    print("Player 1 wins!")

elif (p2 == "rock" and p1 == "scissors") or \
     (p2 == "paper" and p1 == "rock") or \
     (p2 == "scissors" and p1 == "paper"):
    print("Player 2 wins!")

else:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")
