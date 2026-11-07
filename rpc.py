import random
def play_game():
    choices = ["rock", "paper", "scissors"]
    print("game of 🪨rock,📃paper,✂️ Scissors!")
    print("type 'bye' to leave the game the game.\n")
    while True:
        user_choice = input("enter rock, paper, or scissors: ").lower().strip()
        if user_choice == "leave" or user_choice == "bye":
            print("good game nice playing with you ! Goodbye.")
            break
        if user_choice not in choices:
            print("invalid choice. please try again.\n")
            continue
        computer_choice = random.choice(choices)
        print(f"robort chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "🪨rock" and computer_choice == "scissors") or \
             (user_choice == "📃paper" and computer_choice == "rock") or \
             (user_choice == "✂️scissors" and computer_choice == "paper"):
            print("🏆congrats You win this round!\n")
        else:
            print("💻Computer wins this round good luck next time!\n")
if __name__ == "__main__":
    play_game()