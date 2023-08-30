import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def main():
    print("Welcome to Rock, Paper, Scissors Game!")

    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose one: rock, paper, scissors")
        user_choice = input("Your choice: ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("Congratulations! You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Your Score: {user_score} | Computer Score: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Final scores:")
            print(f"Your Score: {user_score} | Computer Score: {computer_score}")
            break

if __name__ == "__main__":
    main()
