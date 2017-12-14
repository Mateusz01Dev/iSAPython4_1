import os, shutil, send2trash

# print(shutil.disk_usage("./"))


# os.unlink("../LICENSE")

# send2trash.send2trash("../LICENSE")

ilosc = 0

for biezacy_folder, podfoldery, pliki in os.walk("../"):
    # print("Obecny katalog:", biezacy_folder)
    #
    # for podfolder in podfoldery:
    #     print(f"podfolder {podfolder} w katalogu {biezacy_folder}")

    for plik in pliki:
        # print(f"plik {plik} w folderze {biezacy_folder}")
        ilosc += 1

print(f"Jest {ilosc} plików")









