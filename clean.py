import pandas as pd
import csv

#declare array to store data
data = []

#read data file
df = pd.read_csv("data.csv")

#remove lines containing blanks
final_data = df.dropna()
final_data.reset_index(drop=True, inplace=True)

#convert file back to CSV format
final_data.to_csv('final_data.csv')

#separate header row (first row) from data rows
headers = final_data[0]
star_data = final_data[1:]

#change masses and radii to solar masses and solar radii
for star in star_data:
    star[2] = float(star[2]) * 0.000954588
    star[3] = float(star[3]) * 0.102763

#update data.csv with cleaned data
with open('data.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

#create final_data.csv with cleaned data
with open('data.csv') as input, open('final_data.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)