def list_shift(valores, promedio):
    for i in range(len(valores)):
        valores[i] = valores[i] + promedio

valores = [2.0, 4.0, 6.0, 8.0]

def calc_avg(valores):
    promedio = sum(valores)/len(valores)
    return promedio

def print_normalized(valores):
    print(valores)

promedio = calc_avg(valores)
list_shift(valores, -promedio)
print_normalized(valores)










