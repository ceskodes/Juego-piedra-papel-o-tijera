import random
from resource import print_options as po

# Option input (USER) and selection (COMPUTER)
def pick_option(options: str):
    print("*"*100)
    user_option = input("What do you choose rock, paper or scissors?: ").lower()
    computer_option = random.choice(options)
    return user_option, computer_option

def game_rules(user_option: str, computer_option: str, options: str):
    # Same option
    if user_option == computer_option:
        if user_option == options[0]:
            po.user_print_rock()
            print((" "*25)+"It's a draw!\n")
            po.comp_print_rock()
        elif user_option == options[1]:
            po.user_print_paper()
            print((" "*25)+"It's a draw!\n")
            po.comp_print_paper()
        elif user_option == options[2]:
            po.user_print_scissors()
            print((" "*25)+"It's a draw!\n")
            po.comp_print_scissors()
            
    # Rock vs Scissors (WIN) / Paper (LOSE)        
    elif user_option == options[0]:
        if computer_option == options[2]:
            po.user_print_rock()
            print((" "*25)+"You win!\n")
            po.comp_print_scissors()
            return "u"
        else:
            po.user_print_rock()
            print((" "*25)+"You lost!\n")
            po.comp_print_paper()
            return "c"
    
    # Paper vs Rock (WIN) / Scissors (LOSE)    
    elif user_option == options[1]:
        if computer_option == options[0]:
            po.user_print_paper()
            print((" "*25)+"You win!\n")
            po.comp_print_rock()
            return "u"
        else:
            po.user_print_paper()
            print((" "*25)+"You lost!\n")
            po.comp_print_scissors()
            return "c"
        
    # Scissors vs Paper (WIN) / Rock (LOSE)    
    elif user_option == options[2]:
        if computer_option == options[1]:
            po.user_print_scissors()
            print((" "*25)+"You win!\n")
            po.comp_print_paper()
            return "u"
        else:
            po.user_print_scissors()
            print((" "*25)+"You lost!\n")
            po.comp_print_rock()
            return "c"
    else:
        print("You should pick a valid option (ROCK, PAPER OR SCISSORS).")

def run_game():
    opt = "yes"
    options = ("rock", "paper", "scissors")
    while opt in {"yes", "y", "ye"}:
        user_score: int = 0
        comp_score: int = 0
        total_games: int = int(input("How many win should the winner have?: "))
        while (user_score != total_games) and (comp_score != total_games):
            user_option, computer_option = pick_option(options)
            if user_option not in options:
                print("Invalid option.\nTry again.")
                continue
            if game_rules(user_option,computer_option, options) == "u":
                user_score+=1
            else:
                comp_score+=1
            print("\n"+(" "*27)+f'{user_score} - {comp_score}')
        opt = input(f'Do you want to play again? (Yes/No): ').lower()

if __name__ == '__main__':
    run_game()
