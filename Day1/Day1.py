
def main():
    
    werte = [int (i) for i in open("day1.txt").readlines()]

    index = 0;
    frequenzen = set()
    aktuelle_summe = 0
    gefunden = 0

    while 1:
        for wert in werte:
            aktuelle_summe += wert
            if aktuelle_summe in frequenzen:
                gefunden = 1
                break
            frequenzen.add(aktuelle_summe)
        if gefunden == 1:
            break
    print(aktuelle_summe)
    a = input("press enter")
    return

if __name__ == "__main__":
    main()