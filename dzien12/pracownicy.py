from dzien12.alternatywny_kons import Pracownik

prac1 = Pracownik("adam", "kowalski", 13)
prac2 = Pracownik.Pracownik("jan", "nowak")
# print(prac2)

prac1.pesel = 498473987983

# print(prac1.pesel)
# print(prac2.pesel)

print(Pracownik.__dict__)
print(prac1.__dict__)
print(prac2.__dict__)

