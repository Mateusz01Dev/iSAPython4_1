file_path = "dane.txt"

# try:
#     with open(file_path, 'r') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print("Podany plik nie istnieje!", e)
# except Exception as e:
#     print("Uuups, następił jakis błąd.", e)
# finally:
#     print("Ta funkcja zawsze sie wykona")


try:
    print("To jest blok try")
    raise ValueError("Sam tworzę wyjątek! typ ValueError")
except ValueError as e:
    print("Złapałem wyjątek", e)
finally:
    print("Zawsze się wykonam.")