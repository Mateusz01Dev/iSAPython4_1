# pierwszy ze sposobów importowania
# importujemy cały moduł
import dzien7.moj_modul.odwracacz


def czy_palindrom(wyraz):
    """Sprawdza czy podany string jest palindromem
    (str)->bool
    """
    wyraz = wyraz.upper()

    # używając zaimporotwanej funkcji musimy dostać się poprzez
    # całą ścieżkę modułu
    odwrocony = dzien7.moj_modul.odwracacz.odwroc_string(wyraz)

    if wyraz == odwrocony:
        return True
    else:
        return False

print(czy_palindrom("kajak"))