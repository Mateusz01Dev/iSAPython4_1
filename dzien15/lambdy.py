
def kapitalizuj(zdanie: str) -> str:
    zdanie = zdanie.strip()
    return zdanie.capitalize()

print(kapitalizuj)

kapital = lambda wyraz: wyraz.capitalize()
print(kapital)
w = kapital("ala")
print(w)