import random

def get_user_choice():
    while True:
        user_choice = input("Choose any one from : rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Choice you made is invalid. Please choose any one from  rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ooopssss!!!!.......It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "yuhuuuuuuuuuu!!!!.....You win!"
    else:
        return "Ooopss!!......You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        play_again = input("Please let me know Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Cya Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
