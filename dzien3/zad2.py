# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

bok_a = int(input("Podaj bok a: "))
bok_b = int(input("Podaj bok b: "))
bok_c = int(input("Podaj bok c: "))

# a < b + c
# b < a + c
# c < a + b

if bok_a < bok_b + bok_c and \
    bok_b < bok_a + bok_c and \
    bok_c < bok_a + bok_b:
    print("Uda się narysować.")

    if bok_a == bok_b and bok_b == bok_c:
        print("trójkąt równoboczny.")
    elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
        print("Trójkąt równoramienny")
    else:
        print("Trójkąt różnoboczny")
