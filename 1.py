import math

n = int(input("Introduce un valor para n: "))
# Calculamos el valor de (3 + raíz de 5) elevado a la n
valor = (3 + math.sqrt(5)) ** n

# Convertimos el valor en una cadena de caracteres
cadena_valor = str(valor)

# Buscamos la posición de la coma en la cadena
posicion_coma = cadena_valor.find(".")

# Tomamos los tres caracteres anteriores a la coma
if posicion_coma > 3:
    tres_digitos_antes = cadena_valor[posicion_coma-3:posicion_coma]
else:
    tres_digitos_antes = "0" * (3 - posicion_coma) + cadena_valor[:posicion_coma]

# Imprimimos los tres últimos dígitos antes de la coma
print("respuesta:", valor)
print("Los tres últimos dígitos antes de la coma son:", tres_digitos_antes)
