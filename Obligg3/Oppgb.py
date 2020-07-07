#Oppgave a
fil_referanse = open("tall_filtrert.txt", "r")
liste = []
linje = fil_referanse.readline()

for linje in fil_referanse:
    liste.append(float(linje))

#oppgave b
antall_tall = len(liste)
print("Datamatierialet inneholder", antall_tall, "tall")

#oppgave c
hoyeste = max(liste)
print("Den høyeste målte verdien er", hoyeste)
minste =  min(liste)
print("Den laveste målte verdien er", minste)

#oppgave d
gjennomsnitt = sum(liste) / len(liste)
print("Gjennomsnittlig verdi av datamaterialet er", gjennomsnitt)

fil_referanse.close()

#Oppgave e

skrive_fil = open("bruk_av_write.txt", "a", encoding="UTF-8")

antall = "Antall:" + str(antall_tall)
snitt = "Gjennomsnitt:" + str(gjennomsnitt)
maks_verdi = "Maksimum:" + str(hoyeste)
min_verdi = "Minimum:" + str(minste)

tekst = antall + "\n" + snitt + "\n" + maks_verdi + "\n" + min_verdi
skrive_fil.write(tekst)

skrive_fil.close()

