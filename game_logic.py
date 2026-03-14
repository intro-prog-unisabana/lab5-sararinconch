
from secret_number import seed_secret_numbers
from secret_number import generate_secret_number
from response import input_response

seed = int(input("Enter a seed number: "))
seed_secret_numbers(seed)
numero_aleatorio = generate_secret_number()
user_input = int(input("What is your guess: "))

contador = 0
while not user_input == numero_aleatorio:
    mensaje = input_response(numero_aleatorio, user_input)
    print(mensaje)
    user_input = int(input("What is your guess: "))
    contador += 1

mensaje = input_response(numero_aleatorio, user_input)       
print(mensaje)
print(f"It took you {contador} tries!")
