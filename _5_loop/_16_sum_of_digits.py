no = 123 # 6

sum = 0

while no != 0:
    mod = no % 10   # 3   | 2         | 1
    sum = sum + mod # 3   | 3 + 2 = 5 | 5 + 1 = 6
    no  = no // 10   # 12 | 1         | 0
    print(sum)

print("Sum of digit : ",sum)

