import os

file_path = "dane.txt"

if os.path.exists(file_path):
    print("Sciezka istnieje, otwieram plik")
    with open(file_path, 'r') as file:
        print(file.read())
else:
    print("Sciezka nie istnieje!")


