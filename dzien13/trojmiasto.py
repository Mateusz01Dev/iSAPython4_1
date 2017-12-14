import requests
from bs4 import BeautifulSoup

adres = "http://trojmiasto.pl"

response = requests.get(adres)

print(response.status_code)

response.raise_for_status()

# print(response.text)

trojmiasto_zupa = BeautifulSoup(response.text, "html.parser")

linki = trojmiasto_zupa.select(".news-list a")
print(linki)

for link in linki:
    # print(link.getText())
    # # print(str(link))
    # print(link.attrs)
    #
    print(f"Wiadomość: {link.get('title')}")
    print(link.get("href"))
    print("------------------\n")


