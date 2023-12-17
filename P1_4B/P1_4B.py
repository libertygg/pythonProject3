import pandas as pd
import csv

OD = pd.read_csv("orderdata_sample.csv")

OD_DF = pd.DataFrame(OD)
OD_DF["Total"] = OD_DF["Quantity"] + OD_DF["Price"] + OD_DF["Freight"]
OD_DF.to_csv("ODS_with_Total.csv")

with open("ODS_with_Total.csv") as ods:
    rdr = csv.DictReader(ods)
    for row in rdr:
        print(row["Quantity"], row["Price"])
