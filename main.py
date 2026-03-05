def distanta_manhattan(v1, v2):
    suma = 0
    for i in range(len(v1)):
        suma += abs(v1[i] - v2[i])
    return suma

f = open("date.txt", "r")
linii = f.readlines()
f.close()

# Transformam liniile din fisier in liste de numere (vectori)
vector1 = [int(x) for x in linii[0].strip().split(",")]
vector2 = [int(x) for x in linii[1].strip().split(",")]

rezultat = distanta_manhattan(vector1, vector2)

# Chestie de securitate: prag de alerta
prag_alerta = 100

if rezultat > prag_alerta:
    print(f"ALERTA: Diferenta de {rezultat} depaseste pragul de securitate!")
else:
    print(f"Sistem stabil. Distanta Manhattan: {rezultat}")
