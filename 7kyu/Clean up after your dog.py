def crap(garden, bags, cap):
    c = 0
    for el in garden:
        for e in el:
            if e == "@":
                c += 1
            if e == "D":
                return "Dog!!"

    return "Clean" if c <= bags * cap else "Cr@p"