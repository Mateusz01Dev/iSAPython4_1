# napisz program wydajacy reszte z zakupow

# zakupy - wartosc, place banknotem
# wydac monetami o nominalach 5 - 0.1
# jak najmniej monet wydac

monety = {5:0, 2:0, 1:0, 0.5:0, 0.2:0, 0.1:0}

wartosc_zak = 11.30
banknot = 20

reszta = round(banknot - wartosc_zak, 2)
print("Wydaj:", reszta)

if reszta < 0:
    print("Za mała wartość banknotu.")
    quit()
elif reszta == 0:
    print("Bez reszty.")
    quit()

for moneta in monety.keys():
    if reszta >= moneta:
        ilosc = reszta // moneta
        monety[moneta] = ilosc
        reszta = round(reszta - (moneta * ilosc), 2)
        print("Tyle reszty jeszcze jest:", reszta)

print("Wydać:")
for moneta, ilosc in monety.items():
    print(f"moneta: {moneta:>4} - {ilosc:>4} sztuk.")
