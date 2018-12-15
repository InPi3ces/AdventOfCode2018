def set_rectangle(field, pos_x, pos_y, size_x, size_y, field_id, liste_uberlappender_ids):
    ueberlappend = 0
    val_current_field = 0
    for x_idx in range(pos_x, pos_x + size_x):
        for y_idx in range(pos_y, pos_y + size_y):

            val_current_field = field[x_idx][y_idx]

            if val_current_field == 0:
                val_current_field = field_id
            elif val_current_field != "X":
                if val_current_field not in liste_uberlappender_ids:
                    liste_uberlappender_ids.append(val_current_field)
                val_current_field = "X"
                ueberlappend = 1
            else:
                ueberlappend = 1

            field[x_idx][y_idx] = val_current_field

        if ueberlappend == 1:
            if field_id not in liste_uberlappender_ids:
                liste_uberlappender_ids.append(field_id)
    return


def main():
    raw_data = [i.rstrip() for i in open("day3b.txt").readlines()]
    w, h = 1000, 1000
    field = [[0 for x in range(w)] for y in range(h)]
    #ueberlappend = 0
    id_liste_ueberlappend = []
    id_liste_alle = []

    for zeile in raw_data:
        field_id = int(zeile.split("@")[0].split("#")[1])
        id_liste_alle.append(field_id)
        zeile = zeile.split("@")[1]
        pos_x = int(zeile.split(",")[0])
        pos_y = int(zeile.split(",")[1].split(":")[0])
        size_x = int(zeile.split(":")[1].split("x")[0])
        size_y = int(zeile.split(":")[1].split("x")[1])
        set_rectangle(field, pos_x, pos_y, size_x, size_y, field_id, id_liste_ueberlappend)

    #for x_idx in range(0, w):
    #    for y_idx in range(0, h):
    #        if field[x_idx][y_idx] == "X":
    #            ueberlappend += 1

    #print(ueberlappend)
    a = [i for i in id_liste_alle if i not in id_liste_ueberlappend]
    print(a)
    input("press enter")
    return

if __name__ == "__main__":
    main()
