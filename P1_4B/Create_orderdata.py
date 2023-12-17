import csv

FN = "orderdata_sample.csv"

values1 = {(123,423,312),(543,345,313)}

with open (FN, "w", encoding="utf-8", newline = "") as ods:

    writer = csv.DictWriter(ods, fieldnames=["Quantity", "Price", "Freight"], quoting=csv.QUOTE_ALL)
    writer.writeheader()

    for VL in values1:
        writer.writerow(dict(Quantity=VL[0],Price=VL[1],Freight=VL[2]))

import os

ASD = os.getcwd()
print(ASD)


