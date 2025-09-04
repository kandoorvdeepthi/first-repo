import random

ROCK='r'
PAPER='p'
SCISSORS='s'

emojis={ROCK:'🪨',PAPER:'📄',SCISSORS:'✂️'}
choices=tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice=input('rock, paper or scissors?(r,p,s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('invalid choice')
    
def display_choice(user_choice,computer_choice):
    print(f'user choice is {emojis[user_choice]}')
    print(f'computer choice is {emojis[computer_choice]}')

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == SCISSORS and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == ROCK and computer_choice == SCISSORS)):
        print('you win!')
    else:
        print('you loose!')

def playing_game():
    while True:

        user_choice=get_user_choice()

        computer_choice=random.choice(choices)

        display_choice(user_choice,computer_choice)

        determine_winner(user_choice,computer_choice)

        should_continue=input('still continue(y/n)?: ').lower()
        if should_continue=='n':
            print('thank you for playing')
            break

playing_game()