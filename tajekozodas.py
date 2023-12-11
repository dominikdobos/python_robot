def bemenet():
    return input("Kérem a robot parancsait (E/D/K/N): ")


def felbontas(irany: str):
    e = 0
    d = 0
    k = 0
    n = 0
    for i in range(len(irany)):
        if irany[i] == 'E':
            e += 1
        elif irany[i] == 'D':
            d += 1
        elif irany[i] == 'K':
            k += 1
        elif irany[i] == 'N':
            n += 1
        else:
            return print("Nem megfelelő parancs! Használd: E/D/K/N")
    iranyok = [e, d, k, n]
    return iranyok


def roviden(iranyok):
    e = 0
    d = 0
    k = 0
    n = 0
    parancsszo = ""
    if iranyok[0] > iranyok[1]:
        e = iranyok[0] - iranyok[1]
        for i in range(e):
            parancsszo += "E"
    elif iranyok[0] < iranyok[1]:
        d = iranyok[1] - iranyok[0]
        for i in range(d):
            parancsszo += "D"

    if iranyok[2] > iranyok[3]:
        k = iranyok[2] - iranyok[3]
        for i in range(k):
            parancsszo += "K"
    elif iranyok[2] < iranyok[3]:
        n = iranyok[3] - iranyok[2]
        for i in range(n):
            parancsszo += "N"

    return print(f"Egy legrövidebb út parancsszava: {parancsszo}")
