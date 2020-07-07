#Deloppgave a)
import matplotlib.pyplot as plt

def Rente(lanet, rente, antall_aar):
    okningstall = 1.0 + rente/100
    verdi = lanet * okningstall ** antall_aar
    return verdi

#Deloppgave b)
def liste(start, slutt):
    return list(range(start, slutt + 1))

liste = liste(0,20)
print(liste)

#Deloppgave c)
lanet = 1 * 10**6
rente = 2.89
ny_liste = []

for antall_aar in liste:
    rente_per_aar = round(Rente(lanet, rente, antall_aar))
    ny_liste.append(rente_per_aar)

print(ny_liste)

#Deloppgave d)

plt.plot(ny_liste)
plt.ylabel("Rente i kr")
plt.xlabel("Antall år")
plt.show()


if __name__ == "__main__":
    Rente(lanet, rente, antall_aar)
