import os

directorio_actual = os.getcwd()
print(f"Current working directory: {directorio_actual}")

import math

numero = int(input("Enter an integer: "))
operación = math.log2(numero)
print(f"Log base 2 of {numero} is: {operación}")

piso = math.floor(operación)
techo = math.ceil(operación)
print(f"Floor: {piso}")
print(f"Ceiling: {techo}")
