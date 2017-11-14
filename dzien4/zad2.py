# policz samogloski i spolgloski
zdanie = input("Podaj jakieś zdanie: ")

samogloski = 0
spolgloski = 0

lista_samogl = "aeiouyąęó"

for litera in zdanie:
    if litera.isalpha():
        if litera in lista_samogl:
            samogloski += 1
        else:
            spolgloski += 1


print(f"Samoglosek: {samogloski}, spółgłosek: {spolgloski}")