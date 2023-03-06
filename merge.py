import csv

#initialise arrays to contain datasets
dataset1 = []
dataset2 = []

#store brown dwarf data in dataset1 array
with open('final_data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        dataset1.append(row)

#store brightest stars data in dataset2 array
with open('brightest_stars.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        dataset2.append(row)

#separate headers and data
headers = dataset1[0]
data1 = dataset1[1:]
data2 = dataset2[1:]

#create file stars.csv containing both datasets
with open('stars.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data1)
    csvwriter.writerows(data2)