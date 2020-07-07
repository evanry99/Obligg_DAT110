class Sporsmaal:
    rett = 0
    def __init__(self, sporsmaal, svaralternativ, svar):
        self.sporsmaal = sporsmaal
        self.svaralternativ = svaralternativ
        self.svar = svar
        self.valgtsvar = 0

    def __str__(self):
        a = f'Spørsmål:\n{self.sporsmaal}\n'
        for k in self.svaralternativ:
            a += f'{k}\n'
        return a

    def sjekksvar(self):
        if self.valgtsvar == self.svar:
            print("du e goe")
            Sporsmaal.rett += 1
        else:
            print("du e nesten goe")

    def velg_svar(self):
        self.valgtsvar = int(input("Velg riktig svar: ")) - 1
        return self.valgtsvar

def lag_sporsmal():
    spm = [Sporsmaal(f'Hva er 1+2?', ['1: 1', '2: 2', '3: 3','4: 82'], 2),
           Sporsmaal(f'Hvordan vet du om hun er en heks?', ['1: Hun har spiss hatt og stor nese', '2: Hun kom flyvende bort på sopelimen sin', '3: Hun gjorde Ariel om til et menneske', '4: Hun veier like mye som en and'], 3),
           Sporsmaal(f'Hva er meningen med livet?', ['1: Å dele glede', '2: Å oppleve så mye som mulig', '3: GAINS!!!', '4: 42'], 3),
           Sporsmaal(f'Var denne oppgaven nødvendig?', ['1: Ja', '2: Nei', '3: Vet ikke', '4: Helt sikkert'], 3),
           Sporsmaal(f'Finner du fisk i havet?', ['1: Hvis du er god til å fiske', '2: Nei', '3: Ja', '4: Hvordan vet vi at fiskene eksisterer. Hvordan vet vi at vi eksisterer?'], 0)]
    return spm


if __name__ == '__main__':
    spm = lag_sporsmal()
    for question in spm:
        print(question)
        question.velg_svar()
        question.sjekksvar()
        print(f'Du har {Sporsmaal.rett} rette svar \n')
