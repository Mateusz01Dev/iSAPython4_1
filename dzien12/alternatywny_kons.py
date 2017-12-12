class Pracownik(object):
    """Definiuje obiekt typu pracownik"""

    ilosc_pracownikow = 0
    roczna_podwyzka = 7

    def __init__(self, imie, nazwisko, stawka):
        """Tworzy instancję Pracownik
        (str, str, int) -> Pracownik"""
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        Pracownik.ilosc_pracownikow += 1

    # def __init__(self, imie, nazwisko):
    #     self.imie = imie
    #     self.nazwisko = nazwisko
    #     self.stawka = 13


    @classmethod
    def zmien_roczna_podwyzka(cls, nowa_wartosc):
        """
        Zmienia wartość domyślnej rocznej podwyżki dla wszystkich pracowników.
        :param nowa_wartosc: podwyżka w p.p.
        :return: None
        """

        if type(nowa_wartosc) != type(int):
            return

        if nowa_wartosc > 18:
            cls.roczna_podwyzka = 18
        else:
            cls.roczna_podwyzka = nowa_wartosc

    @staticmethod
    def sprawdz_pesel(pesel):
        """
        Sprawdza poprawność peselu.
        :param pesel: Numer pesel
        :return: True jeśli pesel poprawny, w innym przypadku False
        """
        if len(pesel) != 11:
            print("pesel nieprawidłowy!")
            return True
        else:
            print("pesel OK")
            return False

    @classmethod
    def Pracownik(cls, imie, nazwisko):
        # tworzymy tymczasowy obiekt
        temp_pracownik = Pracownik(imie, nazwisko, 13)

        # dosotosowujemy
        temp_pracownik.roczna_podwyzka = 10
        # ...
        #
        return temp_pracownik


    def __str__(self):
        return f"Pracownik: {self.nazwisko} ma {self.stawka} PLN"

    def __del__(self):
        """
        Destruktor - wykonywany tuż przed usunieciem obiektu (użycie del)
        """
        Pracownik.ilosc_pracownikow -= 1
        print(f"Pracownik {self.nazwisko} został usunięty")
