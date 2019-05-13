numero_adivinado = False
que_numero = int(input("Jugador 1, òCual quieres que sea el numero que el Jugador 2 adivine?: "))

while numero_adivinado == False:
    adivina_numero = int(input("Jugador 2, ¡Adivina el numero que el jugador 1 establecio!: "))
    if que_numero == adivina_numero:
        numero_adivinado = True

print("¡Adivinaste el numero que el jugador 1 establecio!")