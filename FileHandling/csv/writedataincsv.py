import csv
with open("readdatafromcsv.csv","w",newline='') as csv_file:
    spamwriter=csv.writer(csv_file, delimiter=" ")

    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    readdata=csv.reader(csv_file,delimiter=' ')
    for row in readdata:
        print(readdata)