# oblicz czy rok jest przestępny

# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

# rok = input("Podaj rok: ")
# rok = int(rok)

# zmieniamy stringa (input) na inta
rok = int(input("Podaj rok: "))

if rok % 400 == 0:
    print(f"Rok {rok} jest przestępny.")

elif rok % 4 == 0 and rok % 100 != 0:
    print(f"Rok {rok} jest przestępny.")

else:
    print(f"Rok {rok} nie jest przestępny.")
