import random

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
        print(f'User: {user_option} vs Computer: {computer_option}.\n')
        print("Draw!")

    elif user_option == options[0]:
        if computer_option == options[2]:
            print(f'User: {user_option} vs Computer: {computer_option}.\n')
            print("You win!")
        else:
            print(f'User: {user_option} vs Computer: {computer_option}.\n')
            print(f"Your opponent had {computer_option}, therefore you lost!")
    elif user_option == options[1]:
        if computer_option == options[0]:
            print(f'User: {user_option} vs Computer: {computer_option}.\n')
            print("You win!")
        else:
            print(f'User: {user_option} vs Computer: {computer_option}.\n')
            print(f"Your opponent had {computer_option}, therefore you lost!")
    elif user_option == options[2]:
        if computer_option == options[1]:
            print(f'User: {user_option} vs Computer: {computer_option}.\n')
            print("You win!")
        else:
            print(f'User: {user_option} vs Computer: {computer_option}.\n')
            print(f"Your opponent had {computer_option}, therefore you lost!")
    else:
        print("Invalid option")
    opt = input(f'¿Do you want to play again? (Yes/No): ').lower()