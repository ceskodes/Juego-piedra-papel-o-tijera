import random

user_option = input("¿Piedra, papel o tijera?:").lower()
options = ("piedra", "papel", "tijera")
computer_option = random.choice(options)

print(f'Usuario: {user_option} / Computadora: {computer_option}')

if user_option == computer_option:
    print("Empate!")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("Piedra gana a tijera!")
    else:
        print("Perdiste! el oponente tiene papel")
elif user_option == "tijera":
    if computer_option == "papel":
        print("Tijera gana a papel, ganaste!")
    else:
        print("Perdiste! el oponente saco piedra")
elif user_option == "papel":
    if computer_option == "piedra":
        print("Papel le gana a piedra, ganaste!")
    else:
        print("Perdiste! el oponente saco tijeras!")
else:
    print("Opcion invalida")