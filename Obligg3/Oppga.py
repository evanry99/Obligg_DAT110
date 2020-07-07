
#maks = input('Legg inn maks beløp')
vekt= input('Legg inn vekt på pakken i kilogram')
resultat = 0

while True:
    try:
        vekt = float(vekt)
        if int(vekt) < 0:
            print('Oppgitt vekt på pakken kan ikke være negativ')
        elif int(vekt) == 0:
            break
#        elif int(resultat) > int(maks):
#            resultat -= int(vekt)
#            break
        if int(vekt) > 0 and int(vekt) <= 10:
            print(149)
            resultat += 149

        elif int(vekt) > 10 and int(vekt) <= 25:
            print(268)
            resultat += 268

        elif int(vekt) > 25 and int(vekt) <= 35:
            print(int(381))
            resultat += 381

        elif int(vekt) > 35:
            print('Pakke er for tung til å sendes')

    except ValueError:
        print(vekt + " er ikke en gyldig vekt")

    vekt = input('Legg inn vekt på pakken i kilogram ')

print(int(resultat))

