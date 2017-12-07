class Ubranie(object):
    def __init__(self, firma, rozmiar):
        self.marka = firma
        self.rozmiar = rozmiar


class But(Ubranie):
    def __init__(self, typ_buta, plec):
        super().__init__(firma="polbut", rozmiar="40")
        self.plec = plec


class Szpilka(But):
    def __init__(self, marka, wysokosc):
        super().__init__("szpilka", "kobiecy")
        self.wysokosc = wysokosc


class OdziezWierzchnia(Ubranie):
    pass


class Polbut(But):
    pass


class Plaszcz(OdziezWierzchnia):
    pass


# ubranko = Ubranie("hm", "40")
# print(ubranko)
#
# bucik = But("adidas", "43", "meski")
# print(bucik)

szpileczka = Szpilka("Laboutin", 15)
print(szpileczka.marka)
print(szpileczka.rozmiar)
print(szpileczka.plec)
print(szpileczka.wysokosc)

szpileczka.rozmiar = 36
print(szpileczka.rozmiar)

plaszczyk = Plaszcz("no name", "34")
print(plaszczyk)


def moja_funkcja(marka, rozmiar, kolor):
    if len(marka) > 6:
        print("Dobra marka")
