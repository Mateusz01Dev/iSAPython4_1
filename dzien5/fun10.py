def dodaj_imie(imie, baza=[]):
    imie= imie.upper()
    baza.append(imie)
    return baza

# imiona = ["ANNA", "DAMIAN"]
# imiona = dodaj_imie("andrzej", imiona)
# imiona = dodaj_imie("marek", imiona)
#
# print(imiona)

anglicy = dodaj_imie("john")
print(anglicy)
framcuzi = dodaj_imie("antoin")
print(framcuzi)
rosjanie = dodaj_imie("masza")
print(rosjanie)
