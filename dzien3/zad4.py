# po podaniu nazwy m-ca podaj ilość dni

miesiac = input("Podaj nazwę miesiąca: ")

if miesiac == "kwiecien" or miesiac == "czerwiec" \
        or miesiac == "wrzesień" or miesiac == "listopad":
    print(f"Miesiąc {miesiac} ma 30 dni")

elif miesiac == "luty":
    print("Luty ma 28 lub 29 dni.")

else:
    print(f"Miesiąc {miesiac} ma 31 dni.")

