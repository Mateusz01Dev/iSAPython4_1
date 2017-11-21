import pickle

baza = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
{"imie": "Anna", "nazwisko":"nowak", "wiek":23},
{"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
{"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]

# zapisujemy

with open("baza.pckl", 'wb') as plik:
    pickle.dump(baza, plik)

# otweiramy

odczytana_baza = None

with open("baza.pckl", "rb") as plik:
    odczytana_baza = pickle.load(plik, encoding="utf-8")

print(odczytana_baza)
