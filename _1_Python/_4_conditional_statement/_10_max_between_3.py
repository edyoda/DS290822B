# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:
#     if c>a:
#         print("c is greater",c)
#     else:
#         print(a,"a is greater")
# else:
#     if b>c:
#         print("b is greater",b)
#     else:
#         print("c is greater",c)


no1 = int(input())
no2 = int(input())
no3 = int(input())
if no1 > no2 and no1 > no3:
    print("no1 is greater",no1)
elif no2 > no1 and no2 > no3:
    print("no2 is greater",no2)
elif no3 > no1 and no3 > no2:
    print("no3 is greater",no3)
else:
    print("All the values are equal",no1,no2,no3)

