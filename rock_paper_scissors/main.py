import random
options = ['R','P','S']
check = 'y'
while check == 'y':
    # Get input from user
    user_choice = input("Type 'R' for Rock, 'P' for Paper and 'S' for Scissors:\n").upper()
    # Computer makes its choice
    computer_choice = random.choice(options)
    # Code debug, show computer choice
    print(f"You chose {user_choice}")
    print(f"computer chose {computer_choice}")

    #condition check
    if user_choice == computer_choice:
        print("It is a tie, try again")
    elif (user_choice=='R' and computer_choice=='P') or (user_choice=='P' and computer_choice=='S') or (user_choice=='S' and computer_choice=='R'):
        print('you lose')
    else:
        print('you win')

    #Play again?
    print('Do you want to play again?')
    check = input("Type 'y' for yes, 'n' for no\n").lower()