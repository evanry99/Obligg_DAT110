from Obligg6.Kort import Kortstokk


class Spillere:
    def __init__(self, navn, hand):
        self.navn = navn
        self.hand = hand


class Spill:
    tom_kortstokk = Kortstokk()
    full_kortstokk = Kortstokk()

    def __init__(self):
        self.full_kortstokk.lag_standard_kort()
        self.full_kortstokk.stokk()
        self.spillere = []

    def start_av_spill(self):
        antall_spillere = int(input("Hvor mange spillere ønsker å delta?: "))
        for i in range(antall_spillere):
            navn = input(f"Skriv inn navn på {i + 1}: ")
            hand = []
            for j in range(5):
                trukket_kort = self.full_kortstokk.trekk()
                hand.append(trukket_kort)
            spiller = Spillere(navn, hand)
            self.spillere.append(spiller)

    def spiller_trekk(self, top_card, spiller_hand):
        print(f"For å spille et kort skriv 0. For å trekke et kort skriv 1")
        trekk = int(input(f"Hva ønsker du å gjøre? "))
        if trekk == 0:
            valgt_kort = int(input(f"Velg hvilket kort du vil spille:  "))
            kort = spiller_hand[valgt_kort]
            if kort.verdi == 8:
                self.tom_kortstokk.legg(kort)
                if not spiller_hand:
                    return
                valgt_kort2 = int(input(f"Velg hvilket kort du vil spille:  "))
                kort = spiller_hand[valgt_kort2]
                self.tom_kortstokk.legg(kort)
                del spiller_hand[valgt_kort]
                if valgt_kort2 > valgt_kort:
                    valgt_kort2 -= 1
                del spiller_hand[valgt_kort2]
                return
            else:
                if kort.verdi == top_card.verdi:
                    self.tom_kortstokk.legg(kort)
                    del spiller_hand[valgt_kort]
                    return
                if kort.korttype == top_card.korttype:
                    self.tom_kortstokk.legg(kort)
                    del spiller_hand[valgt_kort]
                    return
                print(f"Det er ikke et gyldig trekk! Gå og legg deg")
            if not spiller_hand:
                return
        trukket_kort = self.full_kortstokk.trekk()
        spiller_hand.append(trukket_kort)
        return

    def spill_spillet(self):
        tur = 0
        top_card = self.full_kortstokk.trekk()
        self.tom_kortstokk.legg(top_card)
        while True:
            if self.full_kortstokk.er_tom():
                top_card = self.tom_kortstokk.trekk()
                self.full_kortstokk = self.tom_kortstokk
                self.full_kortstokk.stokk()
                self.tom_kortstokk = Kortstokk()
                self.tom_kortstokk.legg(top_card)

            if self.full_kortstokk.er_tom():
                print(f"Kortstokken er tom for kort!")
                return

            current_player = self.spillere[tur]
            print(f"Topp kortet er {top_card} ")
            print(f"Det er spiller {current_player.navn} sin tur")
            print(f"Kort på hånd: ")
            for j in range(len(current_player.hand)):
                print(f"{j}: {current_player.hand[j]}")

            self.spiller_trekk(top_card, current_player.hand)
            if not current_player.hand:
                print(f"{current_player.navn} har vunnet!")
                return
            top_card = self.tom_kortstokk.overste_kort()

            tur += 1
            if tur >= len(self.spillere):
                tur = 0

if __name__ == "__main__":
    mitt_spill = Spill()
    mitt_spill.start_av_spill()
    mitt_spill.spill_spillet()
    print(f"Spillet er avsluttet")


