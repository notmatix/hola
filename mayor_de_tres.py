
number_to_guess = 7

oportunidades = 5
user_number = int(input("Adivina un numero: "))
user2 = int(input("Perdiste, pero te quedan {} opotunidades: ".format(oportunidades - 1)))

if number_to_guess != user_number:
    user2
elif number_to_guess == user2:
    print("Has ganado")

