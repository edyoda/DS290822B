# CSV - Comma Seperated Value
# extension - .csv
# all the data in this file are seperated by comma

import csv

with open("B:\\DS290822B\\DS290822B\\_20_csv\\test.csv","r") as file:
    data = csv.reader(file)
    
    header = next(data)
    print(header)

    print()
    rows = []
    for row in data:
        rows.append(row)

    print(rows)

    count = data.line_num
    print("Count : ",count)

    print()
    for i in rows[:2]:
        print(i)
