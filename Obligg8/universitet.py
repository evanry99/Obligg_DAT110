def les_heltall(sporsmaal):
    svar = 0
    fortsett = True
    while fortsett:
        try:
            svar = int(input(sporsmaal))
            fortsett = False
        except ValueError:
            print("Du må skrve et heltall. prøv på nytt.")
    return svar


class Student:
    neste_studentnummer = 1

    def __init__(self, etternavn, fornavn, studieprogram, aarskurs=1):
        self.__studentnummer = Student.neste_studentnummer
        Student.neste_studentnummer += 1
        self.etternavn = etternavn
        self.fornavn = fornavn
        self.studieprogram = studieprogram
        self.aarskurs = aarskurs
        self.emner = []

    @property
    def studentnummer(self):
        return self.__studentnummer

    @property
    def aarskurs(self):
        return self.__aarskurs

    @aarskurs.setter
    def aarskurs(self, nytt_aarskurs):
        if nytt_aarskurs < 1:
            raise ValueError("Årskurs kan ikke være under 1!")
        if nytt_aarskurs > 5:
            raise ValueError("Årskurs kan ikke være over 5!")
        self.__aarskurs = nytt_aarskurs

    def __str__(self):
        return f"Student {self.__studentnummer}: {self.fornavn} {self.etternavn}, studerer {self.studieprogram} i" \
               f" {self.aarskurs} årskurs."

    def legg_til_emner(self, emner):
        print(f"Her er de tilgjengelige emnene: \n")
        while True:
            print(f"Velg deg et emne fra lista: ")
            # System.skriv_emner(self)
            print("Emnene: ")
            for index, e in enumerate(emner):
                print(f"{index}: {e}")
            emnet = input("Hvilket emne?: ")
            if emnet == "":
                break
            emnet = int(emnet)
            self.emner.append(emner[emnet])
        print(f"Studenten har nå valgt ut emnene: ")
        for emne in self.emner:
            print(emne)

    def belastning(self):
        studiepoeng_sum = 0
        for i in self.emner:
            studiepoeng_sum += i.studiepoeng
        # (f"{self.studenter[studenten].fornavn} {self.studenter[studenten].etternavn} kommer til å få {studiepoeng_sum} studiepoeng")
        return studiepoeng_sum

    def emneutskrift(self):
        emneoversikt = ""
        for i in self.emner:
            emneoversikt += i.emnenavn + ", "
        return emneoversikt


class Foreleser:
    def __init__(self, etternavn, fornavn, fagfelt, kontor, epost):
        self.etternavn = etternavn
        self.fornavn = fornavn
        self.fagfelt = fagfelt
        self.kontor = kontor
        self.epost = epost

    def __str__(self):
        return f"Foreleser {self.fornavn} {self.etternavn} i {self.fagfelt}."


class Emne:
    kontakt_epost = None

    def __init__(self, emnekode, emnenavn, studiepoeng=10, semester="H", emneansvarlig=None):
        self.emnekode = emnekode
        self.emnenavn = emnenavn
        self.studiepoeng = studiepoeng
        self.semester = semester
        self.emneansvarlig = emneansvarlig
        self.studenter = []

    def get_students(self):
        return_string = ""
        return_string += f"\nEmnet: {self.emnenavn} inneholder studentene: "
        for i in self.studenter:
            return_string += f"\n{i}"
        return return_string

    def legg_til_epost(self):
        temp = input(f"Skriv inn emneansvarlig sin epost: ")
        if temp == "":
            temp = None
        self.kontakt_epost = temp

    def __str__(self):
        if self.kontakt_epost is None and self.emneansvarlig is not None:
            self.kontakt_epost = self.emneansvarlig.epost

        if self.kontakt_epost is None:
            self.kontakt_epost = "ikke oppgitt"
        return f"Emne {self.emnekode} {self.emnenavn} på {self.studiepoeng} studiepoeng i " \
               f"semester {self.semester} og har {self.emneansvarlig} Kontakt-eposten for emnet er {self.kontakt_epost}"

    def hvem_tar_emnet(self, student_list):
        for s in student_list:
            for e in s.emner:
                if self.emnekode == e.emnekode:
                    self.studenter.append(s)

    def klasseliste(self):
        utskrift = f"{self.emnenavn}: "
        for i in self.studenter:
            utskrift += i.fornavn + "" + i.etternavn + ", "
        return utskrift


class System:
    def __init__(self):
        self.studenter = []
        self.forelesere = []
        self.emner = []

    def skriv_inn_student(self):
        print("Skriv inn student: ")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        studieprogram = input("Studieprogram: ")
        aarskurs = int(input("Årskurs: "))
        studenten = Student(etternavn, fornavn, studieprogram, aarskurs)
        self.studenter.append(studenten)

    def skriv_inn_foreleser(self):
        print("Skriv inn foreleser: ")
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        fagfelt = input("Fagfelt: ")
        kontor = input("Kontor: ")
        epost = input("Epost: ")
        foreleseren = Foreleser(etternavn, fornavn, fagfelt, kontor, epost)
        self.forelesere.append(foreleseren)

    def skriv_inn_emne(self):
        print("Skriv inn emne: ")
        emnekode = input("Emnekode: ")
        navn = input("Navn: ")
        studiepoeng = int(input("Studiepoeng: "))
        semester = input("Semester (H for høst, V for vår): ")
        emnet = Emne(emnekode, navn, studiepoeng, semester)
        self.emner.append(emnet)

    def skriv_studenter(self):
        print("Studentene: ")
        for index, student in enumerate(self.studenter):
            print(f"{index}: {student}")

    def skriv_foreleserne(self):
        print("Foreleserne: ")
        for index, foreleser in enumerate(self.forelesere):
            print(f"{index}: {foreleser}")

    def skriv_emner(self):
        print("Emnene: ")
        for index, emne in enumerate(self.emner):
            print(f"{index}: {emne}")

    def sett_foreleser_for_emne(self):
        self.skriv_foreleserne()
        self.skriv_emner()
        emneindex = les_heltall("Velg emne: ")
        foreleserindex = les_heltall("Velg foreleser: ")
        self.emner[emneindex].emneansvarlig = self.forelesere[foreleserindex]

    def sett_inn_standard_data(self):
        self.forelesere.append(Foreleser("Tøssebro", "Erlend", "Data", "E-442", "et@uis.no"))
        self.forelesere.append(Foreleser("Eielsen", "Arnfinn", "Elektro", "E-454", "ae@uis.no"))
        self.forelesere.append(Foreleser("Hervik", "Sigbjørn", "Matematikk", "E-543", "sh@uis.no"))
        self.emner.append(Emne("DAT110", "Grunnleggende programmering", 10, "V", self.forelesere[0]))
        self.emner.append(Emne("ING100", "Ingeniørfaglig Innføringsemne"))
        self.emner.append(Emne("MAT100", "Matematiske metoder 1"))
        self.emner.append(Emne("RED101", "Kjemi for data og elektro", 5))
        self.emner.append(Emne("RED102", "Fysikk for data og elektro", 5))
        self.studenter.append(Student("Nilsen", "Arne", "Data"))
        self.studenter.append(Student("Torgersen", "Ida", "Data"))
        self.studenter.append(Student("Ås", "Erling", "Elektro"))
        self.studenter.append(Student("Fredriksen", "Anne", "Elektro"))

    def meny(self):
        fortsetter = True
        while fortsetter:
            print("\n meny: ")
            print("0: Skriv inn student")
            print("1: Skriv inn foreleser")
            print("2: skriv inn emne")
            print("3: skriv ut studentene")
            print("4: skriv ut foreleserne")
            print("5: skriv ut emnene")
            print("6: Angi foreleser for et emne")
            print("s: Sett inn standard data (for testing)")
            print("a: avslutt")
            print("a): Legg til emner")
            print("b): Skriv ut totale antall studiepoeng")
            print("c): Skriv ut alle emner studenten har tatt og tar")
            print("d): Skriv ut hvilke studenter som tar emnet")
            print("e): Skriv ut emnet samt alle studenter som tar emnet")
            print("f): Skriv ut kontakt-eposten til gitt emne")
            valg = input("Valg: ")

            if valg == "0":
                self.skriv_inn_student()
            elif valg == "1":
                self.skriv_inn_foreleser()
            elif valg == "2":
                self.skriv_inn_emne()
            elif valg == "3":
                self.skriv_studenter()
            elif valg == "4":
                self.skriv_foreleserne()
            elif valg == "5":
                self.skriv_emner()
            elif valg == "6":
                self.sett_foreleser_for_emne()
            elif valg == "s":
                self.sett_inn_standard_data()
            elif valg == "a":
                fortsetter = False
            elif valg == "a)":
                self.skriv_studenter()
                studenten = input("Hvilken student?: ")
                studenten = int(studenten)
                self.studenter[studenten].legg_til_emner(self.emner)
            elif valg == "b)":
                self.skriv_studenter()
                studenten = input("Hvilken student?: ")
                studenten = int(studenten)
                poengsum = self.studenter[studenten].belastning()
                print(f"Studenten får totalt {poengsum} studiepoeng")
            elif valg == "c)":
                self.skriv_studenter()
                studenten = input("Hvilken student?: ")
                studenten = int(studenten)
                utskrift = self.studenter[studenten].emneutskrift()
                print(f"{self.studenter[studenten]} Samt emnene {utskrift}")
            elif valg == "d)":
                self.skriv_emner()
                emne = input("Hvilket emne?: ")
                emne = int(emne)
                self.emner[emne].hvem_tar_emnet(self.studenter)
            elif valg == "e)":
                self.skriv_emner()
                emne = input("Hvilket emne?: ")
                emne = int(emne)
                studen_oversikt = self.emner[emne].get_students()
                print(studen_oversikt)
            elif valg == "f)":
                self.skriv_emner()
                emne = input("Hvilket emne?: ")
                emne = int(emne)
                self.emner[emne].legg_til_epost()


if __name__ == "__main__":
    system = System()
    system.meny()
