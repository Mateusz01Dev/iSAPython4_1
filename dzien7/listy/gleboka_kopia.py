# import copy
from copy import deepcopy

nabial = ["jajka", "mleko", "twaróg"]
chemia = ["domestos", "płyn do naczyń", "proszek do prania"]

zakupy_listopad = [nabial, chemia]

zakupy_grudzien = deepcopy(zakupy_listopad)
zakupy_styczen = deepcopy(zakupy_listopad)

zakupy_grudzien[0].append("mąka")

print(f"Zakupy listopad: {zakupy_listopad}")
print(f"Zakupy grudzien: {zakupy_grudzien}")
print(f"Zakupy styczen : {zakupy_styczen}")