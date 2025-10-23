import random

def juego_adivina_numero(maximo):
    numero_secreto = random.randint(1, maximo)

    ha_ganado = False
    while not ha_ganado:
        numero = int(input("Adivina el número:"))
        if numero_secreto < numero:
            print("El que he pensado es MENOR")
        elif numero_secreto > numero:
            print("El que he pensado es MAYOR")
        else:
            print("¡Acertaste!")
            ha_ganado = True

juego_adivina_numero(100)