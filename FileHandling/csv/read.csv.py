import csv

with open("readdatafromcsv.csv") as csv_file:
    reader=csv.reader(csv_file,delimiter=" ", quotechar='|')
    for row in reader:
        print(', '.join(row))