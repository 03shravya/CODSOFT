import random
import time


def get_computer_choice():
    return random.choice(["r", "p", "s"])


def determine_winner(user_choice, computer_choice):
    choices = {"r": "rock", "p": "paper", "s": "scissors"}

    if user_choice == computer_choice:
        return f"It's a tie! 🤝 Both chose {choices[user_choice].capitalize()}"
    elif (user_choice == "r" and computer_choice == "s") or \
            (user_choice == "s" and computer_choice == "p") or \
            (user_choice == "p" and computer_choice == "r"):
        return f"🎉 You win! {choices[user_choice].capitalize()} beats {choices[computer_choice].capitalize()}!"
    else:
        return f"💻 Computer wins! {choices[computer_choice].capitalize()} beats {choices[user_choice].capitalize()}! Better luck next time."


def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n🪨📄✂️ Rock-Paper-Scissors Game! 🪨📄✂️")
        user_choice = input("Choose R (rock), P (paper), or S (scissors): ").strip().lower()

        if user_choice not in ["r", "p", "s"]:
            print("❌ Invalid choice. Please choose R, P, or S!")
            continue

        computer_choice = get_computer_choice()
        print("🤖 Computer is thinking...", end="", flush=True)
        time.sleep(1)
        print(f" {computer_choice.upper()}!")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "🎉 You win!" in result:
            user_score += 1
        elif "💻 Computer wins!" in result:
            computer_score += 1

        print(f"📊 Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("🔄 Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("👋 Thanks for playing! See you next time! 🎮")
            break


if __name__ == "__main__":
    play_game()
