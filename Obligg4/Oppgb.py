fil = input("Skriv inn navnet på filen :")
with open(fil, "r") as filen:
    d = dict()
    for line in filen:
        words = line.split(" ")
        line = line.lower()
        for word in words:
            word = word.strip(".,:;)«")
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

    for key in list(d.keys()):
        print(str(key), "=", str(d[key]))
