import random

VALID_CHOICES = ['rock', 'paper', 'scissors', "lizard", "spock"]

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

def player_wins(player, computer):
    return computer in WINNING_COMBOS[player]

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if player_wins(player, computer):
        prompt('You win!')
    elif player == computer:
        prompt("It's a tie!")
    else:
        prompt("Computer wins!")

def display_scores(player, computer):
    prompt(f'Your score: {player}')
    prompt(f'Computer score: {computer}')

player_score = 0
computer_score = 0

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    if player_wins(choice, computer_choice):
        player_score += 1
    elif choice == computer_choice:
        pass
    else:
        computer_score += 1

    display_scores(player_score, computer_score)

    if player_score == 5:
        prompt('You have won the game!')
    elif computer_score == 5:
        prompt("The computer has won the game!")

    while player_score == 5 or computer_score == 5:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('y'):
            player_score = 0
            computer_score = 0
            break
        if answer.startswith('n'):
            break

        prompt("That's not a valid choice")

    if player_score == 5 or computer_score == 5:
        break