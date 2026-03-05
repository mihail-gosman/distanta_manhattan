def distanta_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

puncte = []

f = open("date.txt", "r")
for linie in f:
    coordonate = linie.strip().split(",")
    x = int(coordonate[0])
    y = int(coordonate[1])
    puncte.append([x, y])
f.close()

p1 = puncte[0]
p2 = puncte[1]

rezultat = distanta_manhattan(p1, p2)
print("Distanta din fisier este:", rezultat)
