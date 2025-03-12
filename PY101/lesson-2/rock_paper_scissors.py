import random

VALID_CHOICES = ['rock', 'paper', 'scissors', "lizard", "spock"]

def prompt(message):
    print(f"==> {message}")

def determine_winner(player, computer):
    if ((player == "rock" and
         (computer == "scissors" or computer == "lizard")) or
        (player == "paper" and
         (computer == "rock" or computer == "spock")) or
        (player == "scissors" and
         (computer == "paper" or computer == "lizard")) or
        (player == "lizard" and
         (computer == "paper" or computer == "spock")) or
        (player == "spock" and
         (computer == "rock" or computer == "scissors"))):
        return player
    elif player == computer:
        return None
    else:
        return computer

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if determine_winner(player, computer) == player:
        prompt("You win!")
    elif determine_winner(player, computer) == computer:
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def display_scores(player_score, computer_score):
    prompt(f'Your score: {player_score}')
    prompt(f'Computer score: {computer_score}')

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
    
    if determine_winner(choice, computer_choice) == choice:
        player_score += 1
    elif determine_winner(choice, computer_choice) == computer_choice:
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
        elif answer.startswith('n'):
            break
        else:
            prompt("That's not a valid choice")
        
    if player_score == 5 or computer_score == 5:
        break