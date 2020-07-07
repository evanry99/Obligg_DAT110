import numpy as np
import math
import matplotlib.pyplot as plt


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
            integrasjonsmatrise[i, :] = (integrasjonsmatrise[i - 1, :] +
                                         self.delta_time * endringsvektor)
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
        #        x_posisjon = tilstandsvektor[0]
        #        y_posisjon = tilstandsvektor[1]
        x_fart = tilstandsvektor[2]
        y_fart = tilstandsvektor[3]
        fart = math.sqrt(x_fart ** 2 + y_fart ** 2)
        endringsvektor = np.array([x_fart, y_fart,
                                   -(self.luftmotstand * x_fart * fart),
                                   self.tyngdekraft - (self.luftmotstand * y_fart * fart)])
        return endringsvektor


if __name__ == "__main__":
    integratoren = Integrator(0.01, 0.45)
    basis_kulebane = BasisKulebane(-9.81)
    kulebane_luftmotstand = KulebaneMedLuftmotstand(-9.81, 0.5)
    startvektor = np.array([0, 0, 1, 2])
    basis_kulebane_resultat = integratoren.integrate(basis_kulebane, startvektor)
    kulebane_luftmotstand_resultat = integratoren.integrate(kulebane_luftmotstand, startvektor)
    plt.plot(basis_kulebane_resultat[:, 0], basis_kulebane_resultat[:, 1])
    plt.plot(kulebane_luftmotstand_resultat[:, 0], kulebane_luftmotstand_resultat[:, 1])
    plt.plot(basis_kulebane_resultat[:, 0], basis_kulebane_resultat[:, 1], "o")
    plt.plot(kulebane_luftmotstand_resultat[:, 0], kulebane_luftmotstand_resultat[:, 1], "x")
    plt.legend(("Basis", "Med luftmotstand"))
    plt.show()
