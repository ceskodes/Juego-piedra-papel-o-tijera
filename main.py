import random
import print_options

# Game options.
options = ("rock", "paper", "scissors")
opt = "yes"

while opt == "yes":
    # Option input.
    print("*"*100)
    user_option = input("What do you choose rock, paper or scissors?: ").lower()
    # Pick a random option and is assigned to computer_option.
    computer_option = random.choice(options)

    # Game results
    if user_option == computer_option:
        if user_option == options[0]:
            print_options.user_print_rock()
            print((" "*25)+"It's a draw!\n")
            print_options.comp_print_rock()
        elif user_option == options[1]:
            print_options.user_print_paper()
            print((" "*25)+"It's a draw!\n")
            print_options.comp_print_paper()
        elif user_option == options[2]:
            print_options.user_print_scissors()
            print((" "*25)+"It's a draw!\n")
            print_options.comp_print_scissors()
    elif user_option == options[0]:
        if computer_option == options[2]:
            print_options.user_print_rock()
            print((" "*25)+"You win!\n")
            print_options.comp_print_scissors()
        else:
            print_options.user_print_rock()
            print((" "*25)+"You lost!\n")
            print_options.comp_print_paper()

    elif user_option == options[1]:
        if computer_option == options[0]:
            print_options.user_print_paper()
            print((" "*25)+"You win!\n")
            print_options.comp_print_rock()
        else:
            print_options.user_print_paper()
            print((" "*25)+"You lost!\n")
            print_options.comp_print_scissors()

    elif user_option == options[2]:
        if computer_option == options[1]:
            print_options.user_print_scissors()
            print((" "*25)+"You win!\n")
            print_options.comp_print_paper()
        else:
            print_options.user_print_scissors()
            print((" "*25)+"You lost!\n")
            print_options.comp_print_rock()

    else:
        print("Invalid option")
    opt = input(f'¿Do you want to play again? (Yes/No): ').lower()