row = int(input("Enter rows : "))
cols = int(input("Enter cols : "))

matrix = []
for i in range(row):
    rows = []
    for j in range(cols):
        element = int(input("Enter element : "))
        rows.append(element)
    matrix.append(rows)

print(matrix)