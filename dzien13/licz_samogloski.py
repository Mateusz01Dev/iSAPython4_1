import sys

# print(sys.argv)

if len(sys.argv) != 3:
    print("Błędna liczba argumentów!")
    exit()

zdanie = sys.argv[1]
litera = sys.argv[2]

assert isinstance(zdanie, str)

print(zdanie.count(litera))
