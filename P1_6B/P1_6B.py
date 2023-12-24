import pandas as pd
import glob
import csv
from datetime import datetime
"""
Объединяем файлы.
"""
files = glob.glob('[order]*.csv')

files_data = pd.DataFrame()

for file in files:
    data = pd.read_csv(file)
    data['filename'] = file
    files_data = pd.concat([files_data, data])

#print(files_data)
"""
Создаём новый файл и делаем запись в журнал.
"""
try:
    while True:
        H = files_data.to_csv('new_file_{}.csv'.format(datetime.now().strftime("%d%m%Y_%H%M%S")))
        A = glob.glob('[new]*.csv')
        entry = "File created", A
        with open("Journal.csv", 'a', newline = "") as J:
            writer1 = csv.writer(J, dialect='excel')
            writer1.writerow(entry)
            break
except FileNotFoundError:
    entry2 = "Исходные файлы не найдены."
    with open("Journal.csv", 'a', newline="") as J:
        writer1 = csv.writer(J, dialect='excel')
        writer1.writerow(entry2)












