sciezka = "tekst1.txt"

with open(sciezka) as plik:
    linijka = plik.readline()
    pozycja = plik.tell()
    print(f"Kursor znajduje się w pozycji nr {pozycja}")

    # print(linijka, end='')
    # print("Kolejna linijka")
    # print(plik.read())

    plik.seek(3)
    print(plik.read())

