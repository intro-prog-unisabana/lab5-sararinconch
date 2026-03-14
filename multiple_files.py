from utils import *

mensaje = input("Please type your message\n")
mensajeinvertido = flip(mensaje)
letter = "a"
numeroletra_a = count_letters(mensaje, letter)
mensajecodificado = mensajeinvertido + str(numeroletra_a)

print(f"Your encoded message is: {mensajecodificado}")
