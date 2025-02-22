import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

# Initialize Scores
user_score = 0
computer_score = 0

# Choices Dictionary
choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
emoji = {"r": "🪨", "p": "📄", "s": "✂️"}
hand_images = {"r": "rock.jpeg", "p": "paper.jpeg", "s": "scissor.jpeg"}


# Function to get computer's choice
def get_computer_choice():
    return random.choice(["r", "p", "s"])


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "🤝 It's a Tie!"
    elif (user_choice == "r" and computer_choice == "s") or \
            (user_choice == "s" and computer_choice == "p") or \
            (user_choice == "p" and computer_choice == "r"):
        user_score += 1
        return f"🎉 You Win! {choices[user_choice]} {emoji[user_choice]} beats {choices[computer_choice]} {emoji[computer_choice]}"
    else:
        computer_score += 1
        return f"💻 Computer Wins! {choices[computer_choice]} {emoji[computer_choice]} beats {choices[user_choice]} {emoji[user_choice]}"


# Function to animate hands and play the game
def play_game(user_choice):
    computer_choice = get_computer_choice()

    # Show animation effect
    for _ in range(3):
        user_hand_label.config(image=hand_shaking_img)
        computer_hand_label.config(image=hand_shaking_img)
        root.update()
        time.sleep(0.2)

    # Update images with final choices
    user_hand_label.config(image=hand_images_tk[user_choice])
    computer_hand_label.config(image=hand_images_tk[computer_choice])
    root.update()

    # Display results
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result, fg="yellow")
    score_label.config(text=f"📊 Score - You: {user_score} | Computer: {computer_score}")

    # Show "Next Round" button
    next_round_button.pack(pady=10)


# Function to reset UI for the next round
def next_round():
    user_hand_label.config(image=default_hand_image_tk)
    computer_hand_label.config(image=default_hand_image_tk)
    result_label.config(text="Make your move! 🎭", fg="white")
    next_round_button.pack_forget()


# Function to reset the game completely
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    next_round()
    score_label.config(text="📊 Score - You: 0 | Computer: 0")


# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("550x650")
root.configure(bg="#2B2B2B")

# Load Images
default_hand_image = Image.open("default.jpg").resize((100, 100))  # Default hands
default_hand_image_tk = ImageTk.PhotoImage(default_hand_image)

hand_shaking = Image.open("handshake.png").resize((100, 100))  # Animation effect
hand_shaking_img = ImageTk.PhotoImage(hand_shaking)

hand_images_tk = {}
for key, path in hand_images.items():
    img = Image.open(path).resize((100, 100))
    hand_images_tk[key] = ImageTk.PhotoImage(img)

# Heading
title_label = tk.Label(root, text="🪨📄✂️ Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="#2B2B2B", fg="white")
title_label.pack(pady=20)

# Hand display
hand_frame = tk.Frame(root, bg="#2B2B2B")
hand_frame.pack()

user_hand_label = tk.Label(hand_frame, image=default_hand_image_tk, bg="#2B2B2B")
user_hand_label.grid(row=0, column=0, padx=20)

vs_label = tk.Label(hand_frame, text="VS", font=("Helvetica", 16, "bold"), bg="#2B2B2B", fg="white")
vs_label.grid(row=0, column=1)

computer_hand_label = tk.Label(hand_frame, image=default_hand_image_tk, bg="#2B2B2B")
computer_hand_label.grid(row=0, column=2, padx=20)

# Choice buttons
button_frame = tk.Frame(root, bg="#2B2B2B")
button_frame.pack()

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

rock_button = ttk.Button(button_frame, text="🪨 Rock", style="TButton", command=lambda: play_game("r"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = ttk.Button(button_frame, text="📄 Paper", style="TButton", command=lambda: play_game("p"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = ttk.Button(button_frame, text="✂️ Scissors", style="TButton", command=lambda: play_game("s"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="Make your move! 🎭", font=("Helvetica", 14), bg="#2B2B2B", fg="white")
result_label.pack(pady=20)

# Score label
score_label = tk.Label(root, text="📊 Score - You: 0 | Computer: 0", font=("Helvetica", 12), bg="#2B2B2B", fg="white")
score_label.pack(pady=10)

# Next round button
next_round_button = ttk.Button(root, text="🔄 Next Round", style="TButton", command=next_round)

# Reset game button
reset_button = ttk.Button(root, text="🆕 Reset Game", style="TButton", command=reset_game)
reset_button.pack(pady=20)

# Run GUI
root.mainloop()

