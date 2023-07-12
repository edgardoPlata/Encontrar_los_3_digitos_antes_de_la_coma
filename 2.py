import math
# Pedimos al usuario que ingrese un párrafo
parrafo = input("Ingrese un párrafo: ")

# Dividimos el párrafo en palabras
palabras = parrafo.split()

# Creamos un diccionario para almacenar las palabras y la cantidad de veces que aparecen
frecuencia_palabras = {}

# Recorremos cada palabra del párrafo
for palabra in palabras:
    # Si la palabra ya existe en el diccionario, incrementamos su frecuencia
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    # Si la palabra no existe en el diccionario, la agregamos con una frecuencia inicial de 1
    else:
        frecuencia_palabras[palabra] = 1

# Imprimimos la lista de palabras y su frecuencia
for palabra, frecuencia in frecuencia_palabras.items():
    print(palabra, ":", frecuencia)
