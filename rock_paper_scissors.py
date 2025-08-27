import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'Tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'Win'
    else:
        return 'Lose'

def main():
    print("Rock-Paper-Scissors Game")
    user_score = 0
    computer_score = 0
    while True:
        print("\nChoose: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        if result == 'Win':
            print("You win!")
            user_score += 1
        elif result == 'Lose':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
