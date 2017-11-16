rzeczy = ("pisak", "długopis", "szklanka", "portfel", "myszka")

# Przedmiot: x ma indeks nr: y

# while
indeks = 0
dlugosc = len(rzeczy)

while indeks < dlugosc:
    moja_rzecz = rzeczy[indeks]
    print(f"Przedmiot: {moja_rzecz} ma indeks nr: {indeks}")
    indeks += 1

print(15*"-")
# for
indeks2 = 0
for rzecz in rzeczy:
    print(f"Przedmiot: {rzecz} ma indeks nr: {indeks2}")
    indeks2 += 1

print(15*"-")

# for + enumerate
for indeks3, przedmiot in enumerate(rzeczy):
    print(f"Przedmiot: {przedmiot} ma indeks nr: {indeks3}")

