import numpy as np
import math
import tkinter


class Integrator:
    def __init__(self, delta_time, time_end):
        self.delta_time = delta_time
        self.time_end = time_end
        self.time_start = 0
        self.tidspunkter = np.arange(self.time_start, self.time_end, self.delta_time)

    def integrate(self, function, initial_condition_vector):
        antall_tidssteg = len(self.tidspunkter)
        integrasjonsmatrise = np.zeros((antall_tidssteg, function.vektor_lengde))
        integrasjonsmatrise[0, :] = initial_condition_vector
        for i in range(1, antall_tidssteg):
            endringsvektor = function.evaluate(self.tidspunkter[i], integrasjonsmatrise[i - 1, :])
            integrasjonsmatrise[i, :] = (integrasjonsmatrise[i - 1, :] + self.delta_time * endringsvektor)
        return integrasjonsmatrise


class BasisKulebane:
    def __init__(self, tyngdekraft):
        self.tyngdekraft = tyngdekraft
        self.vektor_lengde = 4

    def evaluate(self, tidspunkt, tilstandsvektor):
        #        x_posisjon = tilstandsvektor[0]
        #        y_posisjon = tilstandsvektor[1]
        x_fart = tilstandsvektor[2]
        y_fart = tilstandsvektor[3]
        endringsvektor = np.array([x_fart, y_fart, 0, self.tyngdekraft])
        return endringsvektor


class KulebaneMedLuftmotstand:
    def __init__(self, tyngdekraft, luftmotstand):
        self.tyngdekraft = tyngdekraft
        self.luftmotstand = luftmotstand
        self.vektor_lengde = 4

    def evaluate(self, tidspunkt, tilstandsvektor):
        x_fart = tilstandsvektor[2]
        y_fart = tilstandsvektor[3]
        fart = math.sqrt(x_fart ** 2 + y_fart ** 2)
        endringsvektor = np.array([x_fart, y_fart,
                                   -(self.luftmotstand * x_fart * fart),
                                   self.tyngdekraft - (self.luftmotstand * y_fart * fart)])
        return endringsvektor


class EnkelAnimasjon:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tegner = tkinter.Canvas(self.hovedvindu, width=600, height=400)
        self.tegner.pack()

        self.x0_posisjon = 10
        self.x1_posisjon = 10 + 10
        self.y0_posisjon = 310
        self.y1_posisjon = 310 + 10

        self.antall_ganger = 0
        self.kula = self.tegner.create_oval(self.x0_posisjon, self.y0_posisjon, self.x1_posisjon, self.y1_posisjon,
                                            fill="blue")
        # self.box = self.tegner.create_rectangle(self.x0_box, self.y0_box, self.x1_box, self.y1_box, fill="red")

        self.kulebane = my_def()
        self.pos_ball = iter(self.kulebane)

        # Denne metoden i hovedvinduet registrerer at den skal kalle metoden "self.flytt_kula"
        # etter 20 millisekunder. Parameterne er (tid i millisekunder, funksjon). Dette kallet
        # starter animasjonen. 20 millisekunder gir en "frame-rate" på 50 oppdateringer
        # i sekundet.
        self.hovedvindu.after(40, self.flytt_kula)

        tkinter.mainloop()

    # Metoden som gjør animasjonen
    def flytt_kula(self):
        self.antall_ganger += 1

        item = next(self.pos_ball)
        item[0] *= 800
        item[1] *= 800

        self.x0_posisjon = 10 + item[0]
        self.x1_posisjon = 10 + item[0] + 10
        self.y0_posisjon = 310 - item[1]
        self.y1_posisjon = 310 - item[1] + 10

        # Flytter kula gjennom å gi den nye koordinater
        # print(f"x: {round(item[0], 1)}  y: {round(item[1], 1)}")
        self.tegner.coords(self.kula, self.x0_posisjon, self.y0_posisjon, self.x1_posisjon, self.y1_posisjon)

        # Legger inn en ny after for å få den til å gjøre neste oppdatering på animasjonen.
        if self.antall_ganger < len(self.kulebane):
            self.hovedvindu.after(40, self.flytt_kula)


def main_def():
    integratoren = Integrator(0.01, 0.45)  # x-axis
    basis_kulebane = BasisKulebane(-9.81)  # tyngdekraft
    kulebane_luftmotstand = KulebaneMedLuftmotstand(-9.81, 0.5)
    startvektor = np.array([0, 0, 1, 2])
    basis_kulebane_resultat = integratoren.integrate(basis_kulebane, startvektor)
    kulebane_luftmotstand_resultat = integratoren.integrate(kulebane_luftmotstand, startvektor)


def my_def():
    integratoren = Integrator(0.01, 0.45)
    basis_kulebane = BasisKulebane(-9.81)
    startvektor = np.array([0, 0, 1, 2])
    basis_kulebane_resultat = integratoren.integrate(basis_kulebane, startvektor)
    return basis_kulebane_resultat


if __name__ == "__main__":
    # main_def()
    gui = EnkelAnimasjon()
