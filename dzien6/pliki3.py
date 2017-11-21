sciezka = "tekst1.txt"

with open(sciezka) as plik:
    print(plik.tell())
    linijki = plik.readlines()

    print(linijki)

    for linijka in linijki:
        print(linijka)