import random
print("Choices are :Rock, Paper, Scissors")

user1 = 0
user2 = 0

while True:
    print(f"Score - You: {user1}, Computer: {user2}")
    user_choice = input("Enter your choice: ").strip().lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!\n")
        user1 += 1
    elif (computer_choice == "rock" and user_choice == "scissors") or \
        (computer_choice == "paper" and user_choice == "rock") or \
        (computer_choice == "scissors" and user_choice == "paper"):
        print("Computer wins!\n")
        user2 += 1

    if user1 == 3:
        print(f"Final Score - You: {user1}, Computer: {user2}\n")
        print("You win the game!")
        break
    elif user2 == 3:
        print(f"Final Score - You: {user1}, Computer: {user2}\n")
        print("Computer wins the game!")
        break