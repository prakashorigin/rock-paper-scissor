"""
WORKFLOW OF PROJECT:
1. User enters a choice (Rock, Paper, Scissor)
2. Computer selects a choice randomly
3. Compare both choices
4. Display the result (Win / Lose / Tie)

GAME RULES:

A. Rock
- Rock vs Rock     → Tie
- Rock vs Paper    → Paper wins
- Rock vs Scissor  → Rock wins

B. Paper
- Paper vs Paper   → Tie
- Paper vs Rock    → Paper wins
- Paper vs Scissor → Scissor wins

C. Scissor
- Scissor vs Scissor → Tie
- Scissor vs Rock    → Rock wins
- Scissor vs Paper   → Scissor wins
"""

import random

# List of possible choices
item_list = ["Rock", "Paper", "Scissor"]

# Taking user input
user_choice = input("Enter your move (Rock, Paper, Scissor): ")

# Computer randomly selects a choice
comp_choice = random.choice(item_list)

# Display both choices
print(f"User choice = {user_choice}")
print(f"Computer choice = {comp_choice}")

# Game logic
if user_choice == comp_choice:
    print("Result: Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock → Computer Wins")
    else:
        print("Rock smashes Scissor → You Win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper → Computer Wins")
    else:
        print("Paper covers Rock → You Win")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor → Computer Wins")
    else:
        print("Scissor cuts Paper → You Win")

else:
    print("Invalid input! Please enter Rock, Paper, or Scissor.")
