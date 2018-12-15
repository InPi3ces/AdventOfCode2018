import re
import distance

distance.hamming("hamming", "hamning")

def check_for_multiple(wort, anzahl):
    bereits_gesucht = []
    bereits_gefunden = [0, 0]
    for buchstabe in wort:
        if buchstabe in bereits_gesucht:
            continue

        anzahl_in_wort = len(re.findall(buchstabe, wort))

        if anzahl_in_wort > 1:
            if not bereits_gefunden[anzahl_in_wort-2]:
                anzahl[anzahl_in_wort-2] += 1
                bereits_gefunden[anzahl_in_wort - 2] = 1
        bereits_gesucht.append(buchstabe)
    return


def main():
    werte = set()
    werte = [i.rstrip() for i in open("day2b.txt").readlines()]
    #checksumme = 0
    #anzahl = [0, 0]

    for zeile in werte:
        for zeile_vergleich in werte:
            if 1 == distance.hamming(zeile, zeile_vergleich):
                print(zeile +"  "+zeile_vergleich)
        #check_for_multiple(zeile, anzahl)

    #checksumme = anzahl[0]
    #for idx in range(1, len(anzahl)):
    #    checksumme *= anzahl[idx]

    #print(checksumme)
    input("press enter")
    return


if __name__ == "__main__":
    main()
