# CSV - Comma Seperated Value
# extension - .csv
# all the data in this file are seperated by comma

import csv

with open("B:\\DS290822B\\DS290822B\\_20_csv\\test.csv","r") as file:
    data = csv.reader(file)
    print(data)

    for row in data:
        print(row)
