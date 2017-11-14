# fizz buzz
# wypisac liczby od 1 do 100 (włącznie)
# zamiast l. podzielnych przez 3 wypisz Fizz
# zamiast liczb podzielnych przez 5 wypisz Buzz
# zamist liczb podzielnych przez 3 i 5 wypisz FizzBuzz

zakres = range(1, 101)

for liczba in zakres:
    if liczba % 15 == 0:
        print("FizzBuzz")
    elif liczba % 5 == 0:
        print("Buzz")
    elif liczba % 3 == 0:
        print("Fizz")
    else:
        print(liczba)


