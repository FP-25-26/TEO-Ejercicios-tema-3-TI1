from collections import namedtuple

Persona = namedtuple("Persona", "nombre, edad")

def lee_personas(n):
    res = []
    for i in range(n): # 0, 1, 2,..., n-1
        nombre = input(f"Nombre de la persona {i+1}:")
        edad = int(input(f"Edad de la persona {i+1}:"))
        res.append(Persona(nombre, edad))
    return res

def edad_media(personas):
    '''
    Recibe una lista de personas y devuelva la edad media.
    '''
    # Esquema de SUMA
    if len(personas) == 0: # Para evitar luego división por cero
        return None # Si la lista está vacía, la media no está definida
    
    suma = 0
    for p in personas:
        suma += p.edad
    return suma / len(personas)

def mayores_18(personas):
    '''Recibe una lista de personas y devuelva una lista ordenada 
    alfabéticamente con los nombres de las personas mayores de edad.
    '''
    nombres = []
    for p in personas:
        if p.edad >=18:
            nombres.append(p.nombre)
    # OPCION 1: sort ordena "in-place"
    #return nombres.sort() <- Esto sería un error
    nombres.sort()
    return nombres

    # OPCION 2: sorted devuelve una nueva lista ordenada
    return sorted(nombres)

def edades_distintas(personas):
    '''Recibe una lista de personas y devuelva una lista con las edades 
    ordenadas de menor a mayor y sin duplicados.
    '''
    edades = set() # {} NO es un conjunto vacío, sino que es un diccionario
    for p in personas:
        edades.add(p.edad)
    # sorted siempre devuelve lista ordenada,
    # independientemente de lo que reciba
    return sorted(edades) 


def persona_mas_joven(personas):
    '''Recibe una lista de personas y devuelve el nombre de la persona
      de menor edad.
    '''
    # Esta variable sirve para guardar en cada momento del bucle,
    # cuál es la persona más joven que ha salido hassta el momento
    persona_menor = None
    for p in personas:
        if persona_menor == None or p.edad < persona_menor.edad:
            persona_menor = p
    return p.nombre

n = 3
personas = lee_personas(n)
print(personas)

print("Edad media:", edad_media(personas))
print("Mayores de 18:",mayores_18(personas))
print("Edades distintas:",edades_distintas(personas))
print("Más joven:",persona_mas_joven(personas))