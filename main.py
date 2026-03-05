def distanta_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

punct_1 = [x1, y1]
punct_2 = [x2, y2]

rezultat = distanta_manhattan(punct_1, punct_2)

print("Distanta Manhattan este:", rezultat)
