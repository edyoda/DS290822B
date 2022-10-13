import csv

# fieldnames = ["rno","name"]
# rows = [[1,"Bharati"],[2,"Sanket"]]

# with open("B:\\DS290822B\\DS290822B\\_20_csv\\test1.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerow(fieldnames) # is used to add header/column
#     writer.writerows(rows)      # is used to add rows





fieldnames = ["rno","name"]
rows = [{"rno":1,"name":"Bharati"},{"rno":1,"name":"Bharati"}]

with open("B:\\DS290822B\\DS290822B\\_20_csv\\test1.csv","w") as file:
    writer = csv.DictWriter(file,fieldnames)
    writer.writeheader()
    writer.writerows(rows)