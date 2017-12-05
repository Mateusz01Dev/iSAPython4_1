from dzien10.zwierze import Zwierze


class Czlowiek(Zwierze):
    def __init__(self, nazwa, wiek):
        super().__init__(nazwa)
        self.wiek = wiek

    def ruszaj_sie(self):
        print(f"{self.nazwa.capitalize()} biegnie.")

    def powiedz(self):
        print(f"Czesc, jestem {self.nazwa.capitaize()}!")

