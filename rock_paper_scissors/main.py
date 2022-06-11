#CODE ALGORITHM

#get input from computer
#get input from user
#check if input from user is correct
    #if not correct:
        #get new input from user until condition is satisfied
    #if correct
        #check if input from user and computer is the same
        # if true:
        # get new input from user and computer until condition is false
        # if the condition is satisfied 
#check if other conditions are satisfied
#ask user if they want to play again
#if yes:
    #run the game again
#if no:
    #end the game


import random
from clearit import clear

options = ['R','P','S']
repeat = True
replay = True

while replay ==  True:
    while repeat == True:
        #get computer and user input
        computer_choice = random.choice(options)
        user_choice = input("Type 'R' for Rock, 'P' for Paper and 'S' for Scissors:\n").upper()
        clear()
        
        #code debug
        #for choice in 
        #code_read = 
        print(f"Player ({user_choice}) : CPU ({computer_choice})")

        #condition check
        if user_choice not in options:
            print('oops! you chose a wrong letter\nchoose again')
        elif user_choice == computer_choice:
            print("It is a tie, choose again")
        else:
            if (user_choice=='R' and computer_choice=='P') or (user_choice=='P' and computer_choice=='S') or (user_choice=='S' and computer_choice=='R'):
                print('you lose')
            else:
                print('you win')
                break
            break
    
    #Play again?
    n = 0
    while n < 20:
        print('Do you want to play again?')
        check = input("Type 'y' for yes, 'n' for no\n").lower()
        if check == 'n':
            replay = False
            print('Goodbye')
            break
        elif check == 'y':
            replay
            break
        else:
            print('You typed a wrong input')
            n+=1