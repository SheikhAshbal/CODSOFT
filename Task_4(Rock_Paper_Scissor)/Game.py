import random

def get_user_choice():
    while True:
        user_choice = input(f"""{user_name} Plz choose 1 option
                            Rock
                            Paper
                            Scissors: """).capitalize()
        
        if user_choice in ['Rock', 'Paper', 'Scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")
                
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def winner_check(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Match Tie!!'
    elif user_choice=="Rock":
        if computer_choice=='Scissors':
            return f'{user_name} win!'
        else:
            return f'{user_name} lose!'
    elif user_choice=="Scissors":
        if computer_choice=='Paper':
            return f'{user_name} win!'
        else:
            return f'{user_name} lose!'
    elif user_choice=="Paper":
        if computer_choice=='Rock':
            return f'{user_name} win!'
        else:
            return f'{user_name} lose!'
def restart_game():
    print("\nRestarting the game. Scores set to zero.\n")
    return 0, 0

def main():
    user_score = 0 
    comp_score = 0 
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n{user_name}'s choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = winner_check(user_choice, computer_choice)
        print(f"\nResult: {result}")

        if result == f'{user_name} win!':
            user_score += 1
        elif result == f'{user_name} lose!':
            comp_score += 1

        print(f"\nScore---->\t{user_name}\t\tComputer: ")
        print(f"\t\t{user_score}\t\t{comp_score}")

        while True:
            try:
                user = int(input("""\nWhat do you want?Press(1/2/3)
                           1.Play Again
                           2.Restart(Scores zero)
                           3.Exit: """))
                if user < 1 or user > 3:
                    print("\nPlease enter a number between 1 and 3.\n")
                elif 1<=user<=3:
                    break
            except:
                print("\nPlease enter a valid integer.")

        if user==1:
            pass
        elif user==2:
            user_score,comp_score=restart_game()
        elif user == 3:
            print("\nThanks for playing!\n")
            break
        
if __name__ == "__main__":
    print("\n------------> Rock-Paper-Scissors Game <-----------\n")
    user_name=input("Enter Your Name:").capitalize()
    print(f"\n{user_name}, Let's Play Rock-Paper-Scissors Game!!\n")
    main()
