
notas = [85, 92, 78]
def promedio_estudiante(notas):
    if notas == []:
        return float()
    Promedio = sum(notas)/len(notas)
    return float(Promedio)
print(promedio_estudiante(notas))



