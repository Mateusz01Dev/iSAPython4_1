liczby = [1,2,3,4,5]

liczby_kwadr = [x ** 2 for x in liczby]
print(liczby)
print(liczby_kwadr)

# list comprehension
kwadr_parz = [x ** 2 for x in liczby if x % 2 == 0]
print(kwadr_parz)

# generator comprehension
kwadraty = (x ** 2 for x in liczby)
print(kwadraty)

for i in kwadraty:
    print(i)