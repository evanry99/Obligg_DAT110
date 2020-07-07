#Oppgave a
try:
    fil_referanse = open("tall_filtrert.txt", "r")
    liste = []
    linje = fil_referanse.readline()
    for linje in fil_referanse:
        liste.append(float(linje))
        linje = float(linje)

#oppgave b
    antall_tall = len(liste)
    print("Datamatierialet inneholder", antall_tall, "tall")

#oppgave c
    hoyeste = max(liste)
    print("Den høyeste målte verdien er", hoyeste)
    minste = min(liste)
    print("Den laveste målte verdien er", minste)

#oppgave d
    gjennomsnitt = sum(liste) / len(liste)
    print("Gjennomsnittlig verdi av datamaterialet er", gjennomsnitt)

#Oppgave e
    skrive_fil = open("bruk_av_write.txt", "a", encoding="UTF-8")

    antall = "Antall:" + str(antall_tall)
    snitt = "Gjennomsnitt:" + str(gjennomsnitt)
    maks_verdi = "Maksimum:" + str(hoyeste)
    min_verdi = "Minimum:" + str(minste)

    tekst = antall + "\n" + snitt + "\n" + maks_verdi + "\n" + min_verdi + "\n"
    skrive_fil.write(tekst)

except IOError as e:
    print("Feil i håndtering av fil: " + str(e))
except UnicodeDecodeError as e:
    print("Feil i koding av tekstfil: " + str(e))
except ValueError as e:
    print("Fila inneholder noe i tall-posisjonen som ikke er et tall! " + str(e))

finally:
    fil_referanse.close()
    skrive_fil.close()
