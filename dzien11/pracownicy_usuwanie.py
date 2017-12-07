from dzien11.pracownik import Pracownik

prac1 = Pracownik("John", "Travolta", 50000)
print(prac1)

prac2 = Pracownik("John", "Turturo", 30000)
print(prac2)

prac3 = Pracownik("John", "Rambo", 90000)
print(prac3)

# print(prac1.ilosc_instancji)
# print(prac2.ilosc_instancji)
# print(prac3.ilosc_instancji)

# del prac2
# print("usunąłem prac 2")
# print(Pracownik.ilosc_instancji)
# print("Koniec programu")
print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)

prac1.zmien_roczna_podwyzka(18)
prac1.roczna_podwyzka = 17
Pracownik.zmien_roczna_podwyzka(22)
Pracownik.roczna_podwyzka = "tysiac piecet sto dziewiecet"

print(prac1.roczna_podwyzka)
print(prac2.roczna_podwyzka)
print(prac3.roczna_podwyzka)

Pracownik.sprawdz_pesel("3827468732648")
