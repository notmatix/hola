operacion = "operacion"

que_operacion = input("¿Que operacion quieres realizar? (Multiplicacion / Division / Suma / Resta: ").lower()
primer_numero = int(input("Escoge tu primer numero: "))
segundo_numero = int(input("Escoge tu segundo numero: "))

resultado = 0

if que_operacion == "multiplicacion":
    resultado = primer_numero * segundo_numero
elif que_operacion == "division":
    resultado = primer_numero / segundo_numero
elif que_operacion == "suma":
    resultado = primer_numero + segundo_numero
elif que_operacion == "resta":
    resultado = primer_numero - segundo_numero

print("El resultado de tu {} es {}".format(que_operacion, resultado))