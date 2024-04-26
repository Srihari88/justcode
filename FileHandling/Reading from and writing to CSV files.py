import csv

data=[
    ["Name", "Age", "Country"],
    ["John", 30, "USA"],
    ["Emma", 25, "Canada"],
    ["Michael", 35, "UK"]
]

csv_file_path=" data.csv"

with open(csv_file_path,"w",newline="") as fh:
    writedata=csv.writer(fh)
    writedata.writerows(data)

print(" Data has been written to the CSV file successfully")


with open("data.csv","r") as fh:
    reader=csv.reader(fh)
    print(" Data from CSV")
    for rows in reader:
        print(rows)