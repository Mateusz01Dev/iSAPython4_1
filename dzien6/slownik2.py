osoby = {}
# print(osoby)
rekordy = [{"imie": "Adam", "nazwisko":"kowalski", "wiek":32},
{"imie": "Anna", "nazwisko":"nowak", "wiek":23},
{"imie": "Jan", "nazwisko":"nowacki", "wiek":34},
{"imie": "Tomasz", "nazwisko":"lato", "wiek":43}]

for indeks, rekord in enumerate(rekordy):
    osoby[indeks] = rekord

print(osoby)

print(len(osoby))

najw_indeks = max(osoby.keys())
print(najw_indeks)

osoby[najw_indeks+1] = {"imie": "Anna", "nazwisko":"nowak", "wiek":23}


