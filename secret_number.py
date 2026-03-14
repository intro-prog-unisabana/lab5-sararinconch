import random

seed = int(input("Enter a seed number:"))

def seed_secret_numbers(seed):
    random.seed(seed)

seed_secret_numbers(seed)

def generate_secret_number(start = 1, end = 100):
    numero_aleatorio = random.randint(start, end)
    return numero_aleatorio









