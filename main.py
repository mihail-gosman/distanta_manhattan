def distanta_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def incarca_date(nume_fisier):
    puncte = []
    f = open(nume_fisier, "r")
    for linie in f:
        coordonate = linie.strip().split(",")
        x = int(coordonate[0])
        y = int(coordonate[1])
        puncte.append([x, y])
    f.close()
    return puncte

if __name__ == "__main__":
    date = incarca_date("date.txt")
    
    if len(date) >= 2:
        rezultat = distanta_manhattan(date[0], date[1])
        print("Distanta Manhattan este:", rezultat)
        
        # Prag de securitate
        if rezultat > 100:
            print("Alerta: Anomalie detectata!")
    else:
        print("Eroare: Fisierul trebuie sa contina cel putin doua puncte.")
