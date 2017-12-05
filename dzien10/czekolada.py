from dzien10.producent import Producent

class Czekolada(object):
    def __init__(self, producent, rodzaj, waga):
        self.producent = producent
        self.rodzaj = rodzaj
        self.waga = waga
        self.cena = None

    def zjedz(self, ilosc_g):
        if ilosc_g >= self.waga:
            self.waga = self.waga - ilosc_g
        else:
            print("Nie ma tyle czekolady")

    def __add__(self, other):
        return self.waga + other.waga

    def __lt__(self, other):
        return self.waga < other.waga

    def __str__(self):
        return f"Czekolada {self.rodzaj} od {self.producent}"