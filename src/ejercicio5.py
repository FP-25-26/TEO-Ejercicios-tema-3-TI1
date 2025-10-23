def indice_primera_aparicion(lista, buscado):
    posicion = -1
    for i, elem in enumerate(lista):
        if elem == buscado:
            posicion = i
    return posicion

lista = ["árbol", "coche", "casa", "peatón"]
for elem in ["casa", "bicicleta"]:
    print(f"Posición de {elem}:{indice_primera_aparicion(lista, elem)}")