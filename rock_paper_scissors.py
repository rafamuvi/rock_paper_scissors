import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    print(f"You choose {action.name}")
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    print(f"The computer choose {action.name}")
    return action

# scores
tie = 0
user_score = 0
computer_score = 0

def choose_winner(user_action, computer_action):
    global tie
    global user_score
    global computer_score

    if user_action == computer_action:
        print(f"Both players selected {user_action.name}!! It's a Tie!!")
        tie += 1

    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes Scissors! You Win!")
            user_score += 1
        else:
            print("Paper covers Rock! You Lose!!")
            computer_score += 1

    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers Rock! You Win!")
            user_score += 1
        else:
            print("Scissors cuts Paper! You Lose!")
            computer_score += 1

    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts Paper! You Win!")
            user_score += 1
        else:
            print("Rock smashes Scissors! You Lose!")
            computer_score += 1
    return tie, user_score, computer_score

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection! Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    choose_winner(user_action, computer_action)

    play_again = input("Play again? (Y/n): ")
    if play_again.lower() != "y" and play_again.lower() != "":
        print(f"==== SCORE ====\nTies: {tie}\nYour score: {user_score}\nComputer score: {computer_score}\n==== END ====")
        break
