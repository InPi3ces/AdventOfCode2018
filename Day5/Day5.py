def collapse(chain):
    idx = 0

    while 1:
        if idx+1 >= len(chain):
            break
        if abs(int(ord(chain[idx])) - int(ord(chain[idx + 1]))) == 32:
            #loeschen
            chain = chain[0:idx]+chain[idx+2:]

            #print(chain)
            if idx > 0:
                idx -= 1
        else:
            idx += 1

    return len(chain)


def main():
    raw_data = open("day5b.txt").read()
    minimum = ["0", 0]
    sammlung = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for char in sammlung:
        laenge = collapse(raw_data[:].replace(char, "").replace(char.upper(), ""))
        if laenge < minimum[1] or minimum[1] == 0:
            minimum[1] = laenge
            minimum[0] = char

    print(minimum)
    input("press enter")
    return

if __name__ == "__main__":
    main()
